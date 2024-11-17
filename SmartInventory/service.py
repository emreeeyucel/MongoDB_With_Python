from abc import ABC, abstractmethod
from settings import collection
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId
from pprint import pprint
import pymongo

class BaseService(ABC):
    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_by_id(self, pk): pass

    @abstractmethod
    def update(self, fiter_value: dict,
               set_value: dict): pass


class CategoryService(BaseService):
    def create(self, item: dict):
        try:
            result = collection.insert_one(item)
            print(f'{result.inserted_id} numaralı ID İLE kaydedildi.')
        except PyMongoError as err:
            print(f'{err.__doc__}')

    def get_all(self):
        try:
            filter = {
                '_BaseEntity__status': {
                    '$in': ['Active', 'Modified']
                }
            }

            projection = {
                '_id': 0,
                'name': 1,
                'description': 1
            }
            for item in collection.find(filter, projection).sort('name', pymongo.ASCENDING):
                pprint(item)
        except PyMongoError as err:
            print(f'{err.__doc__}')

    def get_by_id(self, pk):
        try:

            object_id = ObjectId(pk)

            filter = {
                '$and': [
                    {'_BaseEntity__status': {'$in': ['Active', 'Modified']}},
                    {'_id': object_id}
                ]
            }
            projection = {
                '_id': 0,
                'name': 1,
                'description': 1
            }
            for item in collection.find(filter, projection).sort('name', pymongo.ASCENDING):
                pprint(item)

        except PyMongoError as err:
            print(f'{err.__doc__}')

    def update(self, filter_value: dict, set_value: dict):
        try:
            result = collection.update_one(
                filter_value,
                {'$set': set_value}
            )
            print(f'{result.modified_count} amount record has been effected.!')
        except PyMongoError as err:
            print(f'{err.__doc__}')

