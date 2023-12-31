# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    festival = scrapy.Field()
    hashtag = scrapy.Field()
    caption = scrapy.Field()
    posted_at = scrapy.Field()
    json = scrapy.Field()

    def __repr__(self):
        return repr(
            {
                "id": self["id"],
                "caption": self["caption"],
                "posted_at": self["posted_at"],
                "festival": self["festival"],
                "hashtag": self["hashtag"],
            }
        )
