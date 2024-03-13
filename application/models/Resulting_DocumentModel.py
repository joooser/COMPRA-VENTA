from .base import db, datetime

class Resulting_Document(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    answers_json = db.Column(db.Text, nullable=False)
    plain_text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_type.id', name='fk_document_type_id'), nullable=False)
    document_template_id = db.Column(db.Integer, db.ForeignKey('document_template.id', name='fk_document_template_id'), nullable=False)