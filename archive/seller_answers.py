# seller_answers.py

def get_seller_answers(form_data, questions_seller, questions_seller_a, questions_seller_b, questions_seller_c):
    seller_answers = {}

    # Recoger respuestas para las preguntas generales del vendedor
    for question in questions_seller:
        seller_answers[question] = form_data.get(question)

    # Determinar el tipo de documento y recoger respuestas adicionales
    document_type = form_data.get("El vehiculo me pertenece en virtud de que documento?")
    if document_type == "titulo del inttt":
        for question in questions_seller_a:
            seller_answers[question] = form_data.get(question)
    else:
        for question in questions_seller_b:
            seller_answers[question] = form_data.get(question)

    # Verificar el estado civil y recoger respuestas adicionales si es necesario
    if seller_answers.get("Cual es el estado civil del vendedor?") == "Casado":
        for question in questions_seller_c:
            seller_answers[question] = form_data.get(question)

    return seller_answers