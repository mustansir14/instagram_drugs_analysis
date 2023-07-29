# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import os

# useful for handling different item types with a single interface
from w3lib.http import basic_auth_header


class CustomProxyMiddleware:
    def process_request(self, request, spider):
        request.meta["proxy"] = os.getenv("PROXY")
        request.headers["Proxy-Authorization"] = basic_auth_header(
            os.getenv("PROXY_USER"), os.getenv("PROXY_PASS")
        )
