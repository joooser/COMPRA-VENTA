from flask import session
from .models import db, Question

# Un diccionario que mapea las categorías a nombres legibles
CATEGORY_NAMES = {
    'seller': 'Información del Vendedor',
    'seller_a': 'Información del Vendedor2',
    'seller_b': 'Información del Vendedor3',
    'seller_c': 'Información del Vendedor4',
    'buyer': 'Información del Comprador',
    'car': 'Información del Vehiculo',
    'transaction': 'Información de la Transacción',
}

# Function to initialize the session with the first set of questions
def initialize_question_session():
    session['current_question_set'] = 'seller'  # First set
    session['question_index'] = 0
    session['responses'] = {}

# Function to fetch questions for each set
def fetch_questions(set_name):
    questions = Question.query.filter_by(category=set_name).all()
    session['questions'] = [q.text for q in questions]
    session['question_index'] = 0  # Reset index for new set
    session['current_set_name'] = CATEGORY_NAMES.get(set_name, 'Set de Preguntas')

# Function to store response and advance to next question
def handle_question_response(response):
    questions = session.get('questions', [])
    question_index = session.get('question_index', 0)

    if question_index < len(questions):
        current_question = questions[question_index]
        session['responses'][current_question] = response
        session['question_index'] += 1

        # Imprimir las respuestas actuales para depuración
        print("Respuestas actuales:", session['responses'])


# Function to check if there are more questions in the current set
def has_more_questions():
    questions = session.get('questions', [])
    question_index = session.get('question_index', 0)
    return question_index < len(questions)

# Function to advance to the next question set
def advance_to_next_set():
    # Define the order of question sets
    order = ['seller', 'seller_a', 'seller_b', 'seller_c', 'buyer', 'car', 'transaction']
    current_set = session.get('current_question_set')
    next_index = order.index(current_set) + 1

    if next_index < len(order):
        next_set = order[next_index]
        fetch_questions(next_set)
        session['current_question_set'] = next_set
        session['current_set_name'] = CATEGORY_NAMES.get(next_set, 'Set de Preguntas')
    else:
        # Cuando no hay más sets, se indica que todas las preguntas han sido respondidas
        session.pop('questions', None)
        session['all_questions_answered'] = True

def clear_questions_from_session():
    session.pop('questions', None)
    session.pop('current_question_set', None)
    session.pop('question_index', None)
    session.pop('responses', None)