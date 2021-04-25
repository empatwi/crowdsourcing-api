from flask_restplus import Api
from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp, version='1.0', title='Empatwi Crowdsourcing API',
    default='Root', default_label='Root namespace')