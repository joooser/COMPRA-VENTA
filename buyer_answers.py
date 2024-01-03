# buyer_answers.py

def get_buyer_answers(questions_buyer, questions_car, questions_transaction):
    buyer_answers = {}

    # Hacer preguntas generales al comprador
    for question in questions_buyer:
        buyer_answers[question] = input(question + ": ")

    # Hacer preguntas relacionadas con el vehículo
    for question in questions_car:
        buyer_answers[question] = input(question + ": ")

    # Hacer preguntas relacionadas con la transacción
    for question in questions_transaction:
        buyer_answers[question] = input(question + ": ")

    return buyer_answers