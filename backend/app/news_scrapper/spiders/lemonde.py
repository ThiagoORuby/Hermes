import re
import pytz
import scrapy
from datetime import datetime
from news_scrapper.items import PostItem


class LemondeSpider(scrapy.Spider):
    name = "lemonde"
    allowed_domains = ["lemonde.fr"]
    start_urls = ["https://www.lemonde.fr/"]
    france_tz = pytz.timezone('Europe/Paris')
    brazilia_tz = pytz.timezone('America/Sao_Paulo')

    def parse(self, response):

        posts = response.css("div.article")
        for post in posts:
            url = post.css('a::attr(href)').get()
            if url and not "live" in url:
                yield response.follow(url, self.post_parse)

    def post_parse(self, response):

        item = PostItem()
        news_time = response.css("section.meta__date-reading span::text").get()
        news_time = re.findall(r'\d{1,2}h\d{2}', news_time)[0]
        news_day = re.findall(r'\d{4}/\d{2}/\d{2}', response.url)[0]

        horario_list = list(map(int, news_time.split("h")))
        news_datetime = datetime.strptime(news_day, "%Y/%m/%d").replace(
            hour=horario_list[0], minute=horario_list[1], second=0
        )
        france_time = self.france_tz.localize(news_datetime)
        brazilia_time = france_time.astimezone(self.brazilia_tz)

        item['url'] = response.url
        item['date_published'] = brazilia_time
        title = response.css('h1.article__title')
        item['title'] = title.css('::text').get()
        item['description'] = title.xpath(
            './following-sibling::p/text()'
        ).get()
        item['image_url'] = response.xpath(
            '//article//picture[1]//img/@src'
        ).get()
        item['type'] = response.xpath(
            '//li[@class="breadcrumb__parent breadcrumb__parent--after js-breadcrumb"]//a/text()'
        ).get()

        yield item
