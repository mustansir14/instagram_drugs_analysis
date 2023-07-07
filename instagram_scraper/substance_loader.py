from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from instagram_scraper import models
from instagram_scraper.data import SUBSTANCES
from instagram_scraper.db import DB


class SubstanceLoader:

    def __init__(self) -> None:
        self.db = DB.create()
        self.load_substances()

    def load_substances(self) -> None:
        self.substances = []
        for SUBSTANCE_TYPE, SUBSTANCE_DICT in SUBSTANCES.items():
            substance_type = models.get_or_create(
                self.db, models.SubstanceType, None, name=SUBSTANCE_TYPE
            )
            for SUBSTANCE, NICKNAMES in SUBSTANCE_DICT.items():
                parent_substance = models.get_or_create(
                    self.db,
                    models.Substance,
                    {"substance_type": substance_type},
                    name=SUBSTANCE,
                )
                self.substances.append(parent_substance)

                for NICKNAME in NICKNAMES:
                    try:
                        substance = models.get_or_create(
                            self.db,
                            models.Substance,
                            None,
                            name=NICKNAME,
                            nickname_of_substance_id=parent_substance.id,
                            substance_type=substance_type,
                        )
                    except IntegrityError:
                        continue
                    self.substances.append(substance)
            self.db.commit()
