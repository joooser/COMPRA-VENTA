from .base import db

class Contractor(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    lastname = db.Column(db.String(length=30), nullable=False)
    per_doc_id = db.Column(db.String(length=30), nullable=False)
    birth = db.Column(db.DateTime(), nullable=False)
    civil_status = db.Column(db.String(length=15), nullable=False)
    residence = db.Column(db.String(length=100), nullable=False)
    # ...