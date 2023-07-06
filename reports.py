from typing import List

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from instagram_scraper import models
from instagram_scraper.data import SUBSTANCES


class DrugReportGenerator:
    def __init__(self) -> None:
        self.session = models.get_session()

    def process(self, festivals: List[models.Festival] | None = None) -> None:
        with self.session() as db:
            if festivals is None:
                festivals = db.scalars(select(models.Festival))

            for festival in festivals:
                posts = []
                for hashtag in festival.hashtags:
                    posts.extend(hashtag.posts)

                for post in posts:
                    for SUBSTANCE_TYPE, SUBSTANCE_DICT in SUBSTANCES.items():
                        substance_type = models.get_or_create(
                            db, models.SubstanceType, None, name=SUBSTANCE_TYPE
                        )
                        for SUBSTANCE, NICKNAMES in SUBSTANCE_DICT.items():
                            parent_substance = models.get_or_create(
                                db,
                                models.Substance,
                                {"substance_type": substance_type},
                                name=SUBSTANCE,
                            )
                            self.check_hashtag(parent_substance, post)

                            for NICKNAME in NICKNAMES:
                                try:
                                    substance = models.get_or_create(
                                        db,
                                        models.Substance,
                                        None,
                                        name=NICKNAME,
                                        nickname_of_substance_id=parent_substance.id,
                                        substance_type=substance_type,
                                    )
                                except IntegrityError:
                                    continue
                                self.check_hashtag(substance, post)

            db.commit()

    def check_hashtag(self, substance: models.Substance, post: models.Post) -> None:
        tags = [
            tag.strip("#")
            for tag in post.caption.lower().split()
            if tag.startswith("#")
        ]
        if substance.name.lower() in tags:
            substance.posts.append(post)


if __name__ == "__main__":
    report_generator = DrugReportGenerator()
    report_generator.process()
