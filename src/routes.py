import pymongo
import json

from api import api
from bson.json_util import dumps
from database.db import col
from flask_restplus import Resource, fields, Namespace
from flask import request, render_template, make_response, jsonify

tweet_ns = Namespace('tweet', description='Tweet related operations')

# Model required by flask_restplus for expected data
classification_fields = api.model('Classification', {
    'created_at': fields.DateTime(required=True),
    'classification': fields.Boolean(required=True)
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
        return json.loads(dumps(col.aggregate([{
            '$project': {
                'created_at': 0,
                'keyword': 0,
                'user_location': 0,
                'entities': 0
            }
        }, {'$sample': {'size': 1}}]))), 200

@tweet_ns.route('/<id>')
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
        #TODO: {'_id': {'$oid': id}}
        unclassified_tweet = json.loads(dumps(col.find({'_id': {'$oid': id}})))
        if unclassified_tweet:
            classified_json = request.get_json()
            classification = classified_json['classification']
            return json.loads(dumps(col.update({'_id': id}, {'classification': classification})))
        else:
            return 'Tweet not found', 404
        
