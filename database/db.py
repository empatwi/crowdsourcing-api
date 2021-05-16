import pymongo
from decouple import config

mongo = pymongo.MongoClient(config('MONGODB_ATLAS_CONNECTION_STRING_PROD'), connect=False)
db = pymongo.database.Database(mongo, config('MONGODB_ATLAS_PROD_NAME'))
col = pymongo.collection.Collection(db, config('MONGODB_ATLAS_COLLECTION_NAME'))
