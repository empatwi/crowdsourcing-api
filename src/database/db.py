import pymongo
from decouple import config

mongo = pymongo.MongoClient(config('MONGODB_ATLAS_CONNECTION_STRING_TEST'), connect=False)
#Dev db
#db = pymongo.database.Database(mongo, 'empatwi')
#Test db
db = pymongo.database.Database(mongo, 'test')
col = pymongo.collection.Collection(db, 'tweet')