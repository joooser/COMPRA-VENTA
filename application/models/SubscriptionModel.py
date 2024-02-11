from .base import db

class Subscription(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(length=20), nullable=False)


    def __repr__(self):
        return f'Subscription {self.type}'