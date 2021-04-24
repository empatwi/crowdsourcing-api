from api import bp, api
from flask import Flask
from routes import tweet_ns

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(bp)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_mapping(SECRET_KEY='dev')
app.config['DEBUG'] = True
app.config['RESTPLUS_VALIDATE'] = True
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

api.add_namespace(tweet_ns)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)