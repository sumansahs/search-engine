import pymongo

class MongoPipeline:

    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['search_engine_db']

    def process_item(self, item, spider):
        self.db['scraped_data'].insert_one(dict(item))
        return item
