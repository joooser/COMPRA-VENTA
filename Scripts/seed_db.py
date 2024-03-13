from application import init_app, db
from application.models import Subscription, Role, Questions, DocumentType, SubDocumentType, PaymentTypeDocument

def seed_subscriptions():
    if Subscription.query.count() == 0:
        subscriptions = [
            Subscription(id=1, type='Free'),
            Subscription(id=2, type='Pro'),
        ]
        db.session.bulk_save_objects(subscriptions)
        db.session.commit()
        print("Subscriptions types seeded successfully.")
    else:
        print("Subscriptions types already exist.")

def seed_roles():
    if Role.query.count() == 0:
        roles = [
            Role(id=1, name='Guest'),
            Role(id=2, name='Member'),
            Role(id=3, name='Admin'),
            Role(id=4, name='Root'),
        ]
        db.session.bulk_save_objects(roles)
        db.session.commit()
        print("Roles types seeded successfully.")
    else:
        print("Roles types already exist.")        


def seed_payment_types():
    # Check if there are already entries in the table
    if PaymentTypeDocument.query.count() == 0:
        payment_types = [
            PaymentTypeDocument(name='Efectivo'),
            PaymentTypeDocument(name='Transferencia'),
            PaymentTypeDocument(name='Cheque'),
        ]
        db.session.bulk_save_objects(payment_types)
        db.session.commit()
        print("Payment types seeded successfully.")
    else:
        print("Payment types already exist.")

def seed_sub_document_types():
    compra_venta_vehiculo = DocumentType.query.filter_by(value='Compra_Venta_Vehiculo').first()
    if compra_venta_vehiculo and SubDocumentType.query.count() == 0:
        sub_document_types = [
            SubDocumentType(name='TITULO INTTT', document_type_id=compra_venta_vehiculo.id),
            SubDocumentType(name='DOCUMENTO NOTARIADO', document_type_id=compra_venta_vehiculo.id),
        ]
        db.session.bulk_save_objects(sub_document_types)
        db.session.commit()
        print("Sub-document types seeded successfully.")
    else:
        print("Sub-document types already exist or parent DocumentType not found.")


def seed_document_types():
    if DocumentType.query.count() == 0:
        document_types = [
            DocumentType(id=1, value='Compra_Venta_Vehiculo', label='Compra-Venta Vehiculo'),
            DocumentType(id=2, value='Compra_Venta_Casa', label='Compra-Venta Casa'),
            DocumentType(id=3, value='Compra_Venta_Lancha', label='Compra-Venta Lancha'),
        ]
        db.session.bulk_save_objects(document_types)
        db.session.commit()
        print("DocumentTypes types seeded successfully.")
    else:
        print("DocumentTypes types already exist.")

def seed_questions():
    if Questions.query.count() == 0:
        question_texts = [
            "¿El vehiculo me pertenece en virtud de que documento?",
            "¿Cual es el nombre del vendedor?",
            "¿Cual es la nacionalidad del vendedor?",
            "¿Cual es la cedula del vendedor?",
            "¿Cual es el estado civil del vendedor?",
            "¿Cual es el domicilio del vendedor?",
            "¿Cual es el nombre del conyuge del vendedor?",
            "¿Cual es la nacionalidad del conyuge del vendedor?",
            "¿Cual es la cedula del conyuge del vendedor?",
            "¿Cual es el domicilio conyuge del vendedor?",
            "¿Cual es el numero del titulo del vehiculo?",
            "¿Cual es el numero de forma titulo del vehiculo?",
            "¿De que fecha es el titulo?",
            "¿Que notaria autentico el documento?",
            "¿Bajo que numero quedo autenticado el documento?",
            "¿Bajo que tomo quedo autenticado el documento?",
            "¿En que fecha fue autenticado el documento?",
            "¿Cual es el nombre del comprador?",
            "¿Cual es la nacionalidad del comprador?",
            "¿Cual es la cedula del comprador?",
            "¿Cual es el estado civil del comprador?",
            "¿Cual es el domicilio del comprador?",
            "¿Cual es la marca del vehiculo?",
            "¿Cual es el modelo del vehiculo?",
            "¿Cual es la placa del vehiculo?",
            "¿Cual es el serial motor del vehiculo?",
            "¿Cual es el serial de carroceria del vehiculo?",
            "¿Cual es el año del vehiculo?",
            "¿Cual es el tipo del vehiculo?",
            "¿Cual es el color del vehiculo?",
            "¿Cual es la clase del vehiculo?",
            "¿Cual es el uso del vehiculo?",
            "¿Cual es el precio del vehiculo?",
            "¿En que moneda se hizo el pago el vehiculo?",
            "¿Con que instrumento se pago el vehiculo?",
            "¿Cual es el banco?",
            "¿Cual es el numero de Certificado de Registro del vehiculo?",
            "¿Cual es el numero de forma del Certificado de Registro del vehiculo?",
            "¿Cual es la ciudad donde se raliza el tramite?",
            "¿Cual es el municipio de la notaria?",
            "¿Cual es el estado de la notaria?",
            "¿Cual es el nº de cuenta de donde sale el dinero?",
            "¿Cual es el número de tranferencia?",
            "¿Cual es el nº de cuenta que recibe el dinero?"
        ]
        for text in question_texts:
            if not Questions.query.filter_by(text=text).first():
                question = Questions(text=text, category="Default")
                db.session.add(question)
        db.session.commit()
        print("Questions seeded successfully.")
    else:
        print("Questions already exist.")

if __name__ == '__main__':
    app = init_app()
    with app.app_context():
        seed_subscriptions()
        seed_roles()
        seed_document_types()
        seed_questions()
        seed_payment_types()
        seed_sub_document_types()
        print("Database seeded successfully.")