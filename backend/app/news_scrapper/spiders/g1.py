import scrapy
from news_scrapper.items import PostItem


class G1Spider(scrapy.Spider):

    name = 'g1spider'
    start_urls = ['https://g1.globo.com/']

    def parse(self, response):  # pyright: ignore

        posts = response.css("*.bastian-feed-item")

        for post in posts:
            post_item = PostItem()
            post_item["image_url"] = post.css("img::attr(src)").get()

            link = post.css("a.feed-post-link::attr(href)").get()

            yield response.follow(
                link, self.parse_post, meta={"item": post_item}
            )

    def parse_post(self, response):

        post = response.meta["item"]

        post['title'] = response.css("div.title h1::text").get()
        post['url'] = response.url
        post['description'] = response.css("div.subtitle h2::text").get()
        post['date_published'] = response.css(
            "div.content-publication-data time::attr(datetime)"
        ).get()
        post["type"] = response.css("h1.header-title a::text").get()

        yield post
