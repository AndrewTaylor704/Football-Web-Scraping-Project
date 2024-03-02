import scrapy


class FootballSpider(scrapy.Spider):
    name = "football"
    allowed_domains = ["fbref.com"]
    start_urls = ["https://fbref.com/en/"]

    def parse(self, response):
        pass
