from datetime import datetime

import scrapy
from scrapy.http.response import Response

from instagram_scraper.data import INPUTS
from instagram_scraper.items import PostItem


class InstagramSpider(scrapy.Spider):
    name = "instagram"
    allowed_domains = ["instagram.com"]
    base_url = "https://www.instagram.com/api/v1/tags/logged_out_web_info/?tag_name="
    ids = []

    def start_requests(self):
        for input in INPUTS:
            for hashtag in input["hashtags"]:
                yield scrapy.Request(
                    url=self.base_url + hashtag,
                    meta={"festival": input, "hashtag": hashtag},
                )

    def parse(self, response: Response):
        edge_hashtag_to_media = response.json()["data"]["hashtag"][
            "edge_hashtag_to_media"
        ]
        page_info = edge_hashtag_to_media["page_info"]
        for edge in edge_hashtag_to_media["edges"]:
            post = PostItem()
            post["festival"] = response.meta["festival"]
            post["hashtag"] = response.meta["hashtag"]
            node = edge["node"]
            post["id"] = node["id"]
            post["json"] = node
            try:
                post["caption"] = (
                    node.get("edge_media_to_caption", {})
                    .get("edges", [{}])[0]
                    .get("node", {})
                    .get("text")
                )
            except IndexError:
                post["caption"] = ""
            post["posted_at"] = datetime.fromtimestamp(
                node.get("taken_at_timestamp"))
            yield post

        if page_info["has_next_page"]:
            yield scrapy.Request(
                url=f'{self.base_url}{response.meta["hashtag"]}&max_id={page_info["end_cursor"]}',
                meta={
                    "festival": response.meta["festival"], "hashtag": response.meta["hashtag"]}
            )
