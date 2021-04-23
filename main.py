from flask import Flask, request, Response
from database.db import initialize_db
from database.models.movie import Movie
from database.models.tweet import Tweet

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/empatwi'
}

initialize_db(app)

@app.route('/')
def start():
    return 'Welcome to Empatwi'

@app.route('/tweets')
def get_tweets():
    tweets = Tweet.objects().to_json()
    return Response(tweets, mimetype="application/json", status=200)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)