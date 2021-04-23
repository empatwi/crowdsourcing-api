import pymongo
import json

from decouple import config
from bson.json_util import dumps

mongo = pymongo.MongoClient(config('MONGODB_ATLAS_CONNECTION_STRING'), connect=False)
db = pymongo.database.Database(mongo, 'empatwi')
col = pymongo.collection.Collection(db, 'tweet')
col_results = json.loads(dumps(col.find()))