from pymongo import MongoClient
from models import Category

conn = MongoClient('mongodb://localhost:27017/')

db = conn['SmartInventory']

collection = db['categories']


