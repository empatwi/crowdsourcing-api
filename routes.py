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
    'created_at': fields.DateTime(required=True),
    'tweet_content': fields.String(required=True),
    'user_location': fields.String(required=False),
    'keyword': fields.List(fields.String(), required=True),
    'entities': fields.List(fields.String(), required=False),
    'classification': fields.List(fields.Nested(classification_fields))
})

@tweet_ns.route('/')
class Tweet(Resource):
    @tweet_ns.doc(responses={
        200: 'OK',
        400: 'Bad request',
        500: 'Internal server error'
    })
    @tweet_ns.doc(description='Endpoint to retrieve all tweets')
    def get(self):
        return json.loads(dumps(col.aggregate([{
            '$project': {
                '_id': 0,
                'created_at': 0,
                'keyword': 0,
                'user_location': 0,
                'entities': 0
            }
        }, {'$sample': {'size': 1}}]))), 200