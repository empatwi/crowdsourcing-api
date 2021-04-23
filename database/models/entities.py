from ..db import db

class Entities(db.EmbeddedDocument):
    entities = db.ListField(db.StringField())