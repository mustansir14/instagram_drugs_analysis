from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from tqdm import tqdm

from instagram_scraper import models
from instagram_scraper.data import SUBSTANCES
from instagram_scraper.substance_loader import SubstanceLoader
from instagram_scraper.db import DB


class DrugProcessor:
    def __init__(self) -> None:
        self.substance_loader = SubstanceLoader()
        self.db = DB.create()

    def process(self, festivals: List[models.Festival] | None = None) -> None:

        if festivals is None:
            festivals = self.db.scalars(select(models.Festival))

        for festival in festivals:
            print(f"Processing for festival: {festival.name}")
            posts = []
            for hashtag in festival.hashtags:
                posts.extend(hashtag.posts)
            for post in tqdm(posts):
                self.check_post_for_substances(post)
        self.db.commit()

    def check_post_for_substances(self, post: models.Post):
        for substance in self.substance_loader.substances:
            tags = [
                tag.strip("#")
                for tag in post.caption.lower().split()
                if tag.startswith("#")
            ]
            if substance.name.lower() in tags and post not in substance.posts:
                substance.posts.append(post)
