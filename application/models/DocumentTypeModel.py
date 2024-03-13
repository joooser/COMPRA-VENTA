from .base import db

class DocumentType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), unique=True, nullable=False)
    label = db.Column(db.String(50), nullable=False)

    templates = db.relationship('DocumentTemplate', backref='document_type', lazy=True)
    sub_document_types = db.relationship('SubDocumentType', backref='document_type', lazy=True)