import pymongo
from decouple import config

mongo = pymongo.MongoClient(config('MONGODB_ATLAS_CONNECTION_STRING_DEVELOPMENT'), connect=False)
db = pymongo.database.Database(mongo, config('MONGODB_ATLAS_DEV_NAME'))
col = pymongo.collection.Collection(db, config('MONGODB_ATLAS_COLLECTION_NAME'))
