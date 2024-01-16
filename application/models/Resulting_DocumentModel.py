from .base import db

class Resulting_Document(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    document = db.Column(db.String(255), nullable=False)
    answers_json = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))