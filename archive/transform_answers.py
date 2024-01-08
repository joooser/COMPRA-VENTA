# transform_answers.py

def transform_document(seller_answers, buyer_answers, car_answers, transaction_answers, documento_template):
    """
    Reemplaza los marcadores de posición en el documento con las respuestas correspondientes.

    Args:
    - seller_answers, buyer_answers, car_answers, transaction_answers: Diccionarios con las respuestas.
    - documento_template: String con el template del documento.

    Returns:
    - documento: String del documento con las respuestas insertadas.
    """

    # Combinar todas las respuestas en un solo diccionario
    all_answers = {**seller_answers, **buyer_answers, **car_answers, **transaction_answers}

    # Reemplazar marcadores de posición en el documento
    for key, value in all_answers.items():
        placeholder = f"[{key}]"
        documento_template = documento_template.replace(placeholder, value.upper())

    return documento_template