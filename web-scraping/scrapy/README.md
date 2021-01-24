# scrapy

To run the spider: 
```
$ scrapy crawl quoteSpider
```

To collect scraped content yielded in a JSON file (can also be a csv):
```
$ scrapy crawl quoteSpider -O output.json
```
where
* -O flag: overwrites any existing file
* -o flag: appends new content

To use `scrapy shell` to check the item(s) you want to scrape:
```
$ scrapy shell 'http://quotes.toscrape.com/'
>>> response.xpath("//span[@class='text']")
```

### Bypass restrictions using
* scrapy-user-agents: https://pypi.org/project/scrapy-user-agents/
* proxies
    * can try https://github.com/rejoiceinhope/scrapy-proxy-pool; or
    * create your own list of proxies (maybe search for free proxies)


