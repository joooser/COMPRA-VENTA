from application.models import DocumentTemplate
from flask import current_app as app

def get_document_template(document_type_id, sub_document_type_id, payment_type_id):
    try:
        template = DocumentTemplate.query.filter_by(
            document_type_id=document_type_id,
            sub_document_type_id=sub_document_type_id,
            payment_type_document_id=payment_type_id
        ).first()

        if template:
            return template.template_text
        return "Template not found."
    except Exception as e:
        app.logger.error(f"Error retrieving template: {e}")
        raise
