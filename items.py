from scrapy import Item, Field


class AmazonItem(Item):
    product_name = Field()
    product_price = Field()
    product_url = Field()
