# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem


class AllpointsfpsPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient("localhost",27017)
        db = connection["allpointsfps"]
        self.collection = db["allpointsfps"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
