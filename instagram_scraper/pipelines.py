import json

from scrapy.exceptions import DropItem
from sqlalchemy import select

from instagram_scraper import models
from instagram_scraper.db import DB
from instagram_scraper.drug_processor import DrugProcessor
from instagram_scraper.items import PostItem


class InstagramScraperPipeline:
    def __init__(self) -> None:
        self.drug_processor = DrugProcessor()
        self.db = DB.create()

    def process_item(self, item: PostItem, spider):
        festival = self.get_festival(item)
        if item["posted_at"].date() < festival.start_date or (
            festival.end_date and item["posted_at"] > festival.end_date
        ):
            raise DropItem("Post date not within festival dates")
        hashtag = models.get_or_create(
            self.db, models.Hashtag, None, hashtag=item["hashtag"], festival=festival
        )

        post = self.db.scalar(select(models.Post).where(models.Post.id == item["id"]))
        exists = True
        if not post:
            post = models.Post(id=item["id"])
            exists = False
        if hashtag not in post.hashtags:
            post.hashtags.append(hashtag)
        post.caption = item["caption"]
        post.json = json.dumps(item["json"])
        post.posted_at = item["posted_at"]
        if not exists:
            self.db.add(post)
        self.db.commit()
        self.drug_processor.check_post_for_substances(post)

        return item

    def get_festival(self, item: PostItem) -> models.Festival:
        festival = models.get_or_create(
            self.db,
            models.Festival,
            {
                "name": item["festival"]["festival"],
                "start_date": item["festival"]["start_date"],
                "end_date": item["festival"]["end_date"],
            },
            name=item["festival"]["festival"],
        )

        # update festival if needed
        if festival.start_date != item["festival"]["start_date"]:
            festival.start_date = item["festival"]["start_date"]
            festival.save()
        if festival.end_date != item["festival"]["end_date"]:
            festival.end_date = item["festival"]["end_date"]
            festival.save()

        return festival
