import scrapy
from ..items import MyTutotialItem


class MySpader(scrapy.Spider):
    name = 'quates'
    start_urls = [
        'https://www.yellowpages.com.au/search/listings?clue=Nursery+%26+Garden+Supplies+Wholesale&locationClue=Greater+Sydney%2C+NSW&lat=&lon=&selectedViewMode=list',
    ]

    def parse(self, response):
        items = MyTutotialItem()

        all_div_quote = response.xpath("(//div[contains(@class, 'flow-layout outside-gap-large inside-gap inside-ga')])[1]")
        for quote in all_div_quote:
            title = quote.xpath("//a[@class='listing-name']/text()").extract()
            contact = quote.xpath("((//div[@class='call-to-action-group'])[2]//span[@class='contact-text']/text())[1]").extract()
            address = quote.xpath("(//p[@class='listing-address mappable-address mappable-address-with-poi'])[1]/text()").extract()

            items['title'] = title
            items['contact'] = contact
            items['address'] = address

            yield items