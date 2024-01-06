# main.py
from application.variables import (
    questions_seller, questions_seller_a, questions_seller_b, questions_seller_c,
    questions_buyer, questions_car, questions_transaction,
    documento
)
from application.seller_answers import get_seller_answers
from application.buyer_answers import get_buyer_answers
from application.transform_answers import transform_document
from application.create_pdf import create_pdf

def main():
    # Obtener respuestas del vendedor
    seller_answers = get_seller_answers(questions_seller, questions_seller_a, questions_seller_b, questions_seller_c)

    # Obtener respuestas del comprador, incluyendo detalles del vehículo y la transacción
    buyer_answers = get_buyer_answers(questions_buyer, questions_car, questions_transaction)

    # Combinar todas las respuestas y transformar el documento
    documento_final = transform_document(seller_answers, buyer_answers, documento)

    # Crear el PDF con el documento final
    create_pdf(documento_final, "output.pdf")

if __name__ == "__main__":
    main()