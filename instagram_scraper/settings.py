# Scrapy settings for instagram_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "instagram_scraper"

SPIDER_MODULES = ["instagram_scraper.spiders"]
NEWSPIDER_MODULE = "instagram_scraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "instagram_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "authority": "www.instagram.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-prefers-color-scheme": "dark",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"14.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "viewport-width": "982",
    "x-ig-app-id": "936619743392459",
    "x-ig-www-claim": "0",
    "x-requested-with": "XMLHttpRequest",
    "cookie": 'mid=ZHYHuwAEAAGoIgYrqwQx9be9qE-3; ig_did=F767FA46-58E5-43F4-B9AF-151C8EF3626B; ig_nrcb=1; datr=uQd2ZMs52lITIxRb4j7qQkEe; fbm_124024574287414=base_domain=.instagram.com; csrftoken=x0BXVaIMCCLK3qprAPHYQrXz3sbVf5KF; ds_user_id=1403201432; shbid="3043\0541403201432\0541720162773:01f747756fcf95bdff5540c8670022c7088309ec2f6949c0688e74f06a3b37ff6cbb2338"; shbts="1688626773\0541403201432\0541720162773:01f76fea50e967c0b5d9e5bf7ad5a5a150d8980f0bc8404c4e7760f12578873768e0e8d6"; dpr=2; sessionid=1403201432%3AuPnnOMzsCk71Jl%3A23%3AAYerWcRAPmRz0byyf6uixY3H1MTt-ZhFcjMu9SAnYg; fbsr_124024574287414=6HMXDkhL18-pkdFCCFK__P7xTbC-UMrgukE_d4lvkUQ.eyJ1c2VyX2lkIjoiMTAwMDAyOTEwODMxOTYwIiwiY29kZSI6IkFRQWc5NUNxaENfQ2l2MURZZzR4enhsdV9CWi1uMTdWYTI3MFY3blVGNm0wU3NYQ25jb1JjMG5tVnZQSEpZLUhLNEw0ZkI0akJLZUcwOERDTEQwempPcmxBZ1I4bnpER1EwMXk1OUt0ZFFUVmlIV1RxOFBBcUV0eUd3eWtXQlNDY2JQVEJPWXBrT1RyQlhxQzRpSjJsaWdCX0RKRHV5ajA0UzhjNnl6LTNPWHdUN1VBcUFwMDVXdzItbFpMRzEwU1NRMjJhclpKM05LYVozMTJpTmJJbFh1UEVIVHBmeDI2eGdzT1hvY1BwRWtpMmYyd1pRVG43RF95bk8tWG9lTjJCUGd3OWktMzAwNkQ1elp5R0NTZlptZlF3UU9Vb0ZTRmdNa2NOaTRmcDgxRll1cXNYSHZaMlpxU3F3aWpTUDN3ajhQUXhPM0ktSURuMjItVkxzVlYxZkp6Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUJLMjJ2Mng2T1NZY2ZQYlM1UlA1SHNEdVQ4bFpDSDY1SHJGem5OVzdFN2VKYTZLbG9aQW9FU3FTazRGZ1I0V1pCN3BYWkNWR0t5TFpBTnJUNE9jbmJuQ3RaQUdwUlFBTGZGalBLUjNDMkttT0FqWG1HVmo3cDVIZkVVSERpbUZ3SWs3RTk2VVd6Z2VCQXVyVjJNajQ3MWhXWVFUYzRpbzJZejVWSW1CNXRweTN6R1RHeU5uZ1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODg3MjMyNTh9; fbsr_124024574287414=e8fEuHHOeodJuNFxazl9xg6TKHTtF8ByWITPm39-Eho.eyJ1c2VyX2lkIjoiMTAwMDAyOTEwODMxOTYwIiwiY29kZSI6IkFRQmFCRjM2dno3MEVGUFYtZlZvZ3pkZHlMT1pZcmNGNjR1X3Y3RklFdnBuRHh5NjRoTjJLU1hMbnZxTFlLN05kcVdDdVh0QlJvcUdGc1ZzSWU0aW16OFpPZm5XaHpJQkxlWkwtQkRRMlZlckFXNWVRSU1fMkg0Y1J5aWJKOHRFS3A0UHRacXN0MnFCT0p3bGhrSElqYkQ0TXVmbFRSM3BHb1N0MlVfTHg5dTVsa1N4YzRmYU8zVHRtMjQ5RlI5WGpoblFrRFU4TXpvMXIydEdCem5VY3A4Q3NieTE1N1pGUVdXS29fOXU5VDgxUVhoWWRNcXRtSWxlQ2p4Q0hsUmJGc2dzMnAyN0xKS0haZWVGaW5ZOVFKZVc3TE5tTkQweGczajZVU2k3M2U5b20zVk1rWXpWLUh5SHRZaHUyVGRzdWhvSnZEQnkxQzNqSk44TkZYYXRMZTV1Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUVrZ1pDVnFjOHJycHBhZzdwUjJhcHdjMVBrUDNQc0haQjhwM2xQVkVKaUg3YndNeU5STjRvdGhJZmZLeXVSOWNjZE50aUlTRHNjaFY1WkNFT2tUUTFKbnJ2SmlnV1FxSVc0WVd3eVlQRjRFWkM0SWZEVEpNdWVQWG96c1pCRjlmaTRZQ1pDNWgyQUUxMVFwajh3UUFIWTZaQmNYc3diM0pBZEoxN3NCOEE1NUtHcUxQaWpGaGdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjg4NzIzNTg2fQ; rur="FRC\0541403201432\0541720259634:01f750c33e4b50d3b36df9044c26f4479dee846788976f0f3f8ebf692df2fe1f9a4bd890"'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "instagram_scraper.middlewares.InstagramScraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "instagram_scraper.middlewares.InstagramScraperDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "instagram_scraper.pipelines.InstagramScraperPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
