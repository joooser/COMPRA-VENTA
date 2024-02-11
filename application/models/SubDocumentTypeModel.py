from .base import db

class SubDocumentType(db.Model):
    __tablename__ = 'sub_document_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_type.id'), nullable=False)

    templates = db.relationship('DocumentTemplate', backref='sub_document_type', lazy=True)