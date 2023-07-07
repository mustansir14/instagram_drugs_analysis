from __future__ import annotations

from sqlalchemy.orm import Session
import os
import logging
import sqlalchemy
from instagram_scraper.models import Base

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class DB(Session):
    __instance = None

    def __init__(self) -> None:
        """ Virtually private constructor. """

        if DB.__instance is not None:
            raise Exception(
                "This class is a singleton, use DB.create()")
        else:
            DB.__instance = self

        engine = sqlalchemy.create_engine(url=os.getenv("DATABASE_URL"))
        Base.metadata.create_all(bind=engine)
        super().__init__(bind=engine)

    @staticmethod
    def create() -> DB:
        if DB.__instance is None:
            DB.__instance = DB()

        return DB.__instance

    def __del__(self) -> None:
        self.close()
