# scraped items
# extracted data -> temporary containers (items) -> storing in database

import scrapy

class quoteItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
