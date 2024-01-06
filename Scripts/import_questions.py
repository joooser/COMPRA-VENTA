# Description: This file is used to import the questions and the document template to the database.

import sys
sys.path.append('C:/Users/Alfonzo/Documents/GitHub/COMPRA-VENTA')

from application import app, db 
from application.models import Question, DocumentTemplate
from application.variables import (
    questions_seller, questions_seller_a, questions_seller_b, questions_seller_c,
    questions_buyer, questions_car, questions_transaction, documento
)

# Function to add questions
def add_questions(questions, category):
    for question_text in questions:
        question = Question(text=question_text, category=category)
        db.session.add(question)

# Wrap database operations in application context
with app.app_context():
    # Adding questions to the database
    add_questions(questions_seller, 'seller')
    add_questions(questions_seller_a, 'seller_a')
    add_questions(questions_seller_b, 'seller_b')
    add_questions(questions_seller_c, 'seller_c')
    add_questions(questions_buyer, 'buyer')
    add_questions(questions_car, 'car')
    add_questions(questions_transaction, 'transaction')
    # Adding the document template
    document_template = DocumentTemplate(template_text=documento)
    db.session.add(document_template)
    # Committing changes to the database
    db.session.commit()