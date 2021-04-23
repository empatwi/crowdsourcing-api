from ..db import db
from .classification import Classification
from .entities import Entities

class Tweet(db.Document):
    created_at = db.DateTimeField(required=True)
    tweet_content = db.StringField(required=True, unique=True)
    user_location = db.StringField(required=False)
    keyword = db.ListField(db.StringField(), required=True)
    classification = db.ListField(db.EmbeddedDocumentField(Classification))
    entities = db.EmbeddedDocumentField(Entities)