from .base import db

class DocumentTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<DocumentTemplate {self.id}>'