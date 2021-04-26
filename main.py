from api import bp, api
from flask_cors import CORS, cross_origin
from flask import Flask
from routes import tweet_ns

app = Flask(__name__, instance_relative_config=True)
cors = CORS(app)

app.register_blueprint(bp)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_AUTOMATIC_OPTIONS'] = True
app.config.from_mapping(SECRET_KEY='dev')
app.config['DEBUG'] = True
app.config['RESTPLUS_VALIDATE'] = True
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

cross_origin(automatic_options=True)

api.add_namespace(tweet_ns)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)