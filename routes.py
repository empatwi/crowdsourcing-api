import json

from api import api
from bson.json_util import dumps
from bson.objectid import ObjectId
from database.db import col
from flask_restplus import Resource, fields, Namespace
from flask import request

tweet_ns = Namespace('tweet', description='Tweet related operations')

# Model required by flask_restplus for expected data
classification_fields = api.model('Classification', {
    'created_at': fields.DateTime(required=True),
    'classification': fields.Boolean(required=True)
})

reported_fields = api.model('Reported', {
    'reported_at': fields.DateTime(required=True),
    'reported': fields.Boolean(required=True)
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
            {'$match': { '$or': [
                {'classification.2': {'$exists': False}},
                {'reported.2': {'$exists': False}}
            ]}}, 
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
            json.loads(dumps(col.update(
                {'_id': ObjectId(id)}, 
                {'$push': {'classification': classification}}
            )))
            return json.loads(dumps(col.find({'_id': ObjectId(id)}))), 200
        else:
            return 'Tweet not found', 404        

@tweet_ns.route('/reported/<id>/')
class TweetReported(Resource):
    @tweet_ns.doc(responses={
        200: 'OK',
        400: 'Bad request',
        404: 'Tweet not found',
        500: 'Internal server error'
    })
    @tweet_ns.expect(reported_fields, validate=True)
    @tweet_ns.doc(description='Sends reported tweet data to database')
    def put(self, id):
        reported_tweet = json.loads(dumps(col.find({'_id': ObjectId(id)})))
        if reported_tweet:
            reported = request.get_json()
            json.loads(dumps(col.update(
                {'_id': ObjectId(id)},
                {'$push': {'reported': reported}}
            )))
            return json.loads(dumps(col.find({'_id': ObjectId(id)}))), 200
        else:
            return 'Tweet not found', 404