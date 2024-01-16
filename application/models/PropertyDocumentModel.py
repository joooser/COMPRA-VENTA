from .base import db

class PropertyDocument(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    notary = db.Column(db.String(length=30), nullable=False)
    n_auth = db.Column(db.Integer(), nullable=False)
    tome = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    # ...