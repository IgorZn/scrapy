import scrapy
from ..items import MyTutotialItem


class MySpader(scrapy.Spider):
    name = 'quates'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        items = MyTutotialItem()

        all_div_quote = response.css('div.quote')
        for quote in all_div_quote:
            title = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tag = quote.css('.tag::text').extract()

            q_items = [title, author, tag]
            items = q_items

            yield {
                'title': title,
                'author': author,
                'tag': tag
            }