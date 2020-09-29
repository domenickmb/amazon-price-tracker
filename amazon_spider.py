import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    def parse(self, response):
        self.item['product_price'] = response.xpath(
            '//span[@id="price_inside_buybox"]/text()').re_first(r'\$(\d+,?.*)\s*')
        self.item['product_name'] = response.xpath(
            '//span[@id="productTitle"]/text()').get().strip()
        self.item['product_url'] = response.url
