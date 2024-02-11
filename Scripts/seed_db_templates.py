# seed_db_templates.py
from application import init_app, db
from application.models import DocumentTemplate, DocumentType, SubDocumentType, PaymentTypeDocument
from .assemble_templates import get_assembled_templates

def seed_templates():
    document_type = DocumentType.query.filter_by(value='Compra_Venta_Vehiculo').first()
    if not document_type:
        print("DocumentType 'Compra_Venta_Vehiculo' not found.")
        return

    assembled_templates = get_assembled_templates()

    for sub_doc_name, payment_name, template_text in assembled_templates:
        sub_document_type = SubDocumentType.query.filter_by(name=sub_doc_name, document_type=document_type).first()
        payment_type_document = PaymentTypeDocument.query.filter_by(name=payment_name).first()

        if not sub_document_type or not payment_type_document:
            print(f"Missing data for {sub_doc_name} or {payment_name}. Skipping template.")
            continue

        template = DocumentTemplate(
            template_text=template_text,
            document_type_id=document_type.id, 
            sub_document_type_id=sub_document_type.id, 
            payment_type_document_id=payment_type_document.id  # Corrected field name
        )
        db.session.add(template)

    db.session.commit()
    print("Document templates seeded successfully.")

if __name__ == '__main__':
    app = init_app()
    with app.app_context():
        seed_templates()
