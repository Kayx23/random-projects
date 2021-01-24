import scrapy
from ..items import quoteItem

# short form
class testSpider(scrapy.Spider):  # subclass scrapy.Spider
    name = 'quoteSpider'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):

        for quote_block in response.xpath("//div[@class='quote']"):

            items = quoteItem()
            # need a . here to make it context specific; otherwise, return the same item every time
            items['title'] = quote_block.xpath(".//span[@class='text']/text()").get()      #.strip(u'\u201c\u201d')
            items['author'] = quote_block.xpath(".//small[@class='author']/text()").get()
            items['tags'] = quote_block.xpath(".//div[@class='tags']/a/text()").getall()   # might be multiple tags

            yield items
        
        # going to the next page
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            # can directly use the relative url with response.follow
            yield response.follow(next_page, callback=self.parse)