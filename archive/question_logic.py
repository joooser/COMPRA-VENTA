from flask import session
from .models import db, Question, DocumentTemplate
import logging

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
    set_initial_question_set('seller')

def set_initial_question_set(set_name):
    session['current_question_set'] = set_name
    session['question_index'] = 0
    session['responses'] = {}

# Function to fetch questions for each set
def fetch_questions(set_name):
    questions = Question.query.filter_by(category=set_name).all()
    session['questions'] = [q.text for q in questions]
    reset_question_index()
    update_current_set_name(set_name)

def reset_question_index():
    session['question_index'] = 0

def update_current_set_name(set_name):
    session['current_set_name'] = CATEGORY_NAMES.get(set_name, 'Set de Preguntas')

# Function to store response and advance to next question
def handle_question_response(response):
    questions = session.get('questions', [])
    question_index = session.get('question_index', 0)
    store_response_and_advance_index(questions, question_index, response)

def store_response_and_advance_index(questions, question_index, response):
    if question_index < len(questions):
        current_question = questions[question_index]
        session['responses'][current_question] = response
        session['question_index'] += 1

        # Imprimir las respuestas actuales para depuración
        print("Respuestas actuales:", session['responses'])


# Function to check if there are more questions in the current set
def has_more_questions():
    return session.get('question_index', 0) < len(session.get('questions', []))

# Function to advance to the next question set
def advance_to_next_set():
    # Define the order of question sets
    order = ['seller', 'seller_a', 'seller_b', 'seller_c', 'buyer', 'car', 'transaction']
    current_set = session.get('current_question_set')
    try:
        next_set = order[order.index(current_set) + 1]
        fetch_questions(next_set)
        session['current_question_set'] = next_set
    except IndexError:
        end_question_session()

def end_question_session():
    session.pop('questions', None)
    session['all_questions_answered'] = True

def clear_questions_from_session():
    keys_to_remove = ['questions', 'current_question_set', 'question_index', 'responses']
    for key in keys_to_remove:
        session.pop(key, None)

def fetch_document_template():
    template = DocumentTemplate.query.filter_by(id=1).first()
    return template.template_text if template else "Document template not found."

# Helper function to start document creation process
def start_document_creation():
    if 'questions' not in session:
        initialize_question_session()
        fetch_questions(session['current_question_set'])
    return fetch_document_template()

# Function to make the content inside the curly braces editable and bold
def make_content_editable(text):
    return replace_text_with_html_input(text, editable=True)

def replace_editable_fields(text):
    return replace_text_with_html_input(text, editable=False)

def replace_text_with_html_input(text, editable):
    parts = re.split(r'(\{.*?\})', text)
    for i, part in enumerate(parts):
        if part.startswith('{') and part.endswith('}'):
            editable_text = part.strip('{}')
            if editable:
                parts[i] = f'<strong><input type="text" value="{editable_text}" class="editable-field" /></strong>'
            else:
                response = session['responses'].get(editable_text, '')
                parts[i] = f'<strong>{response}</strong>'
    return ''.join(parts)



logging.basicConfig(filename='app.log', level=logging.INFO)

# Use logging in your application
logging.info('Info message')
logging.error('Error message')
