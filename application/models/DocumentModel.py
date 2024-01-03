from .base import db

class Document(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    contractor_seller_id = db.Column(db.Integer(), db.ForeignKey('contractor.id'), nullable=False)
    contractor_buyer_id = db.Column(db.Integer(), db.ForeignKey('contractor.id'), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    type_payment = db.Column(db.String(length=30), nullable=False)
    # Aquí puedes añadir relaciones con ForeignKey si es necesario
    # ...