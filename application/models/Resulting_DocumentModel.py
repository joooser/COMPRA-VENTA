from .base import db, datetime

class Resulting_Document(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    document = db.Column(db.String(255), nullable=False)
    answers_json = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))