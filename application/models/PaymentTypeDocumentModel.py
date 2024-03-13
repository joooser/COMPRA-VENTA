from .base import db

class PaymentTypeDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    templates = db.relationship('DocumentTemplate', backref='payment_type_document', lazy=True)