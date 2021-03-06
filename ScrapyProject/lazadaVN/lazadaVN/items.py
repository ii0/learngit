# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class LazadavnItem(Item):
    collection = 'lazada_vn_0518_test05'
    pro_name = Field()
    pro_price = Field()
    pro_review = Field()
    pro_url = Field()
    category = Field()
    page = Field()
    page_url = Field()