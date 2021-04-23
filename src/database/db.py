import pymongo
from decouple import config

mongo = pymongo.MongoClient(config('MONGODB_ATLAS_CONNECTION_STRING'), connect=False)
db = pymongo.database.Database(mongo, 'empatwi')
col = pymongo.collection.Collection(db, 'tweet')