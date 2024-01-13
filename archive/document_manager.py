# document_manager.py

import json
from flask import session
from .models import db, Resulting_Document, DocumentTemplate

def save_responses_to_db():
    document_title = session.get('document_title', 'Sin Título')
    responses_json = json.dumps(session.get('responses', {}))

    # Imprimir el JSON final para depuración
    print("JSON de respuestas final:", responses_json)

    new_document = Resulting_Document(title=document_title, answers_json=responses_json)
    db.session.add(new_document)
    db.session.commit()

    return new_document.id  # Retornamos el ID para usarlo luego.

def get_template_and_fill_content(document_id):
    document = Resulting_Document.query.get(document_id)
    template = DocumentTemplate.query.first()

    # Cargar las respuestas como un diccionario
    answers = json.loads(document.answers_json)

    # Obtener todas las posibles claves de preguntas de la plantilla
    template_keys = [word.strip('{}') for word in template.template_text.split() if word.startswith('{') and word.endswith('}')]

    # Crear un diccionario con todas las claves y 'No especificado' como valor predeterminado
    default_answers = {key: 'No especificado' for key in template_keys}

    # Combinar respuestas con valores predeterminados
    full_answers = {**default_answers, **answers}

    filled_content = template.template_text.format(**full_answers)
    return filled_content

# Aquí puedes añadir la función de generar PDF si es necesario.
