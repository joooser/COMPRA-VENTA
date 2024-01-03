# buyer_answers.py

def get_buyer_answers(form_data, questions_buyer, questions_car, questions_transaction):
    buyer_answers = {}

    # Recoger respuestas para las preguntas generales del comprador
    for question in questions_buyer:
        buyer_answers[question] = form_data.get(question)

    # Recoger respuestas relacionadas con el vehículo
    for question in questions_car:
        buyer_answers[question] = form_data.get(question)

    # Recoger respuestas relacionadas con la transacción
    for question in questions_transaction:
        buyer_answers[question] = form_data.get(question)

    return buyer_answers