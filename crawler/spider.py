import scrapy
from scrapy.crawler import CrawlerProcess
from pipelines import MongoPipeline

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http//www.google.com']

    def parse(self, response):
        for title in response.css('title::text').getall():
            yield {'title': title}

process = CrawlerProcess(settings={
    'ITEM_PIPELINES': {'pipelines.MongoPipeline': 300},
})

process.crawl(MySpider)
process.start()
