# seller_answers.py

def get_seller_answers(questions_seller, questions_seller_a, questions_seller_b, questions_seller_c):
    seller_answers = {}

    # Hacer las preguntas generales al vendedor
    for question in questions_seller:
        seller_answers[question] = input(question + ": ")

    # Pregunta específica para el tipo de documento
    document_type_question = "El vehiculo me pertenece en virtud de que documento?"
    document_type = input(document_type_question + " (Elija 'titulo del inttt' o 'documento notariado'): ")
    seller_answers[document_type_question] = document_type

    # Preguntas adicionales basadas en el tipo de documento
    if document_type == "titulo del inttt":
        for question in questions_seller_a:
            seller_answers[question] = input(question + ": ")
    else:
        for question in questions_seller_b:
            seller_answers[question] = input(question + ": ")

    # Verificar el estado civil y hacer preguntas adicionales si es necesario
    if seller_answers["Cual es el estado civil del vendedor?"] == "Casado":
        for question in questions_seller_c:
            seller_answers[question] = input(question + ": ")

    return seller_answers