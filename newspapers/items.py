# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class NewspapersItem(Item):
    # define the fields for your item here like:
    # name = Field()
    subtitle = Field()
    title    = Field()
    text     = Field()
    category = Field()
    date     = Field()
    editor   = Field()
    pass
