import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
        }

    def parse(self, response):
        self.item['product_price'] = response.xpath(
            '//span[@id="price_inside_buybox"]/text()').re_first(r'\$(\d+,?.*)\s*')
        self.item['product_name'] = response.xpath(
            '//span[@id="productTitle"]/text()').get().strip()
        self.item['product_url'] = response.url
