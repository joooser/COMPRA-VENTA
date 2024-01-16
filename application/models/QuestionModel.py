from .base import db

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'seller', 'buyer', 'car', etc.

    def __repr__(self):
        return f'<Question {self.text}>'