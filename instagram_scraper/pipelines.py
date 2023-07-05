import json

from sqlalchemy import select

from instagram_scraper import models
from instagram_scraper.items import PostItem


class InstagramScraperPipeline:
    def __init__(self) -> None:
        self.session = models.get_session()

    def process_item(self, item: PostItem, spider):
        with self.session() as db:
            festival = models.get_or_create(
                db,
                models.Festival,
                {
                    "name": item["festival"]["festival"],
                    "start_date": item["festival"]["start_date"],
                    "end_date": item["festival"]["end_date"],
                },
                name=item["festival"]["festival"],
            )
            print(festival)
            hashtag = models.get_or_create(
                db, models.Hashtag, None, hashtag=item["hashtag"], festival=festival
            )

            post = db.scalar(select(models.Post).where(models.Post.id == item["id"]))
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
                db.add(post)
            db.commit()

        return item
