from ..db import db

class Classification(db.EmbeddedDocument):
    created_at = db.DateTimeField(required=True)
    classification = db.BooleanField(required=True)