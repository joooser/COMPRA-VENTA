from .base import db

class DocumentTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template_text = db.Column(db.Text, nullable=False)
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_type.id'), nullable=True)
    sub_document_type_id = db.Column(db.Integer, db.ForeignKey('sub_document_type.id'), nullable=True)
    payment_type_document_id = db.Column(db.Integer, db.ForeignKey('payment_type_document.id'), nullable=True)