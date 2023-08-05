# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazondatasetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductItems(scrapy.Item):
    url =scrapy.Field()
    product_name =scrapy.Field()
    product_price =scrapy.Field()
    percentage_off =scrapy.Field()
    orignal_price =scrapy.Field()
    ratings =scrapy.Field()
    image_url =scrapy.Field()
    product_description =scrapy.Field()