import json

from api import api
from bson.json_util import dumps
from bson.objectid import ObjectId
from utils.custom_fields import NullableBoolean
from database.db import col
from flask_restplus import Resource, fields, Namespace
from flask import request

tweet_ns = Namespace('tweet', description='Tweet related operations')

# Model required by flask_restplus for expected data
classification_fields = api.model('Classification', {
    'created_at': fields.DateTime(required=True),
    #'classification': fields.Boolean(required=True)
    'classification': NullableBoolean(),
    'reported': NullableBoolean()
})

tweet_fields = api.model('Tweet', {
    'tweet_content': fields.String(required=True),
    'classification': fields.List(fields.Nested(classification_fields))
})

@tweet_ns.route('/')
class Tweet(Resource):
    @tweet_ns.doc(responses={
        200: 'OK',
        400: 'Bad request',
        500: 'Internal server error'
    })
    @tweet_ns.doc(description='Retrieves a random tweet')
    def get(self):
        return json.loads(dumps(col.aggregate([
            {'$match': {
                'classification.2': {'$exists': False}
            }}, 
            {'$project': {
                '_id': {'$toString': '$_id'},
                'tweet_content': 1
            }},
            {'$sample': {'size': 1}}
        ])))

@tweet_ns.route('/<id>/')
class TweetClassification(Resource):
    @tweet_ns.doc(responses={
        200: 'OK',
        400: 'Bad request',
        404: 'Tweet not found',
        500: 'Internal server error'
    })
    @tweet_ns.expect(classification_fields, validate=True)
    @tweet_ns.doc(description='Sends classification data to database')
    def put(self, id):
        unclassified_tweet = json.loads(dumps(col.find({'_id': ObjectId(id)})))

        if unclassified_tweet:
            classification = request.get_json()
            if classification['classification'] is not None:
                json.loads(dumps(col.update(
                    {'_id': ObjectId(id)}, 
                    { '$push': {
                        'created_at': classification['created_at'],
                        'classification': classification['classification']
                    }}
                )))
            elif classification['reported'] is not None:
                json.loads(dumps(col.update(
                    {'_id': ObjectId(id)},
                    {'$push': {}}
                )))
            return json.loads(dumps(col.find({'_id': ObjectId(id)}))), 200
        else:
            return 'Tweet not found', 404