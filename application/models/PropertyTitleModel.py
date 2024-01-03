from .base import db

class PropertyTitle(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    n_title = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    form = db.Column(db.String(length=30), nullable=False)
    # ...