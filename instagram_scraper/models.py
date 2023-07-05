import os
from datetime import date, datetime
from typing import List, Optional, Tuple

from dotenv import load_dotenv
from sqlalchemy import (BigInteger, Column, DateTime, ForeignKey, Table,
                        create_engine, func)
from sqlalchemy.orm import (DeclarativeBase, Mapped, Session, mapped_column,
                            relationship, sessionmaker)

load_dotenv()


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )


class Festival(Base):
    __tablename__ = "festival"
    name: Mapped[str] = mapped_column(unique=True)
    start_date: Mapped[date]
    end_date: Mapped[Optional[date]]

    hashtags: Mapped[List["Hashtag"]] = relationship(
        "Hashtag", back_populates="festival"
    )


hashtag_post = Table(
    "hashtag_post",
    Base.metadata,
    Column("hashtag_id", ForeignKey("hashtag.id"), primary_key=True),
    Column("post_id", ForeignKey("post.id"), primary_key=True),
)


class Hashtag(Base):
    __tablename__ = "hashtag"
    hashtag: Mapped[str] = mapped_column(unique=True)
    festival_id: Mapped[int] = mapped_column(ForeignKey("festival.id"))

    festival: Mapped[Festival] = relationship("Festival", back_populates="hashtags")
    posts: Mapped[List["Post"]] = relationship(
        "Post", secondary="hashtag_post", back_populates="hashtags"
    )


class Post(Base):
    __tablename__ = "post"

    caption: Mapped[str]
    posted_at: Mapped[datetime]
    json: Mapped[str]

    hashtags: Mapped[List[Hashtag]] = relationship(
        "Hashtag", secondary="hashtag_post", back_populates="posts"
    )


class SubstanceType(Base):
    __tablename__ = "substance_type"

    name: Mapped[str] = mapped_column(unique=True)

    substances: Mapped[List["Substance"]] = relationship(
        "Substance", back_populates="substance_type"
    )


class Substance(Base):
    __tablename__ = "substance"

    name: Mapped[str] = mapped_column(unique=True)
    substance_type_id: Mapped[int] = mapped_column(ForeignKey("substance_type.id"))

    substance_type: Mapped[SubstanceType] = relationship(
        "SubstanceType", back_populates="substances"
    )
    nicknames: Mapped[List["SubstanceNickname"]] = relationship(
        "SubstanceNickname", back_populates="substance"
    )


class SubstanceNickname(Base):
    __tablename__ = "substance_nickname"

    nickname: Mapped[str] = mapped_column(unique=True)
    substance_id: Mapped[int] = mapped_column(ForeignKey("substance.id"))

    substance: Mapped[Substance] = relationship("Substance", back_populates="nicknames")


def get_session() -> sessionmaker:
    engine = create_engine(url=os.getenv("DATABASE_URL"))
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)


def get_or_create(
    session: Session, model: Base, defaults: dict | None = None, **kwargs
) -> Base:
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance
    else:
        kwargs |= defaults or {}
        instance = model(**kwargs)
        try:
            session.add(instance)
            session.commit()
        except (
            Exception
        ):  # The actual exception depends on the specific database so we catch all exceptions. This is similar to the official documentation: https://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance
        else:
            return instance