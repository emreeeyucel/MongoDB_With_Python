from pymongo import MongoClient
from models import Category

conn = MongoClient('mongodb://localhost:27017/')

db = conn['CRUD_db']

collection = db['categories']


