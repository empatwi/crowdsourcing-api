from api import api
from database.db import col_results
from flask_restplus import Resource, fields, Namespace
from flask import request, render_template, make_response, jsonify

tweet_ns = Namespace('tweet', description='Tweet related operations')

# Model required by flask_restplus for expected data
tweet_fields = api.model('Tweet', {
    'created_at': fields.DateTime(required=True),
    'tweet_content': fields.String(required=True),
    'user_location': fields.String(required=False),
    'keyword': fields.List(fields.String(), required=True),
    'entities': fields.List(fields.String(), required=False),
    #classification: fields.List([created_at, bool], required=True)
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
        return col_results, 200