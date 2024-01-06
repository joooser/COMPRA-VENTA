from flask import session
from .models import db, Question

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

# Function to store response and advance to next question
def handle_question_response(response):
    questions = session.get('questions', [])
    question_index = session.get('question_index', 0)

    if question_index < len(questions):
        current_question = questions[question_index]
        session['responses'][current_question] = response
        session['question_index'] += 1

# Function to check if there are more questions in the current set
def has_more_questions():
    return session.get('question_index', 0) < len(session.get('questions', []))

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
    else:
        # No more sets, could redirect to generate document or similar
        session.pop('questions', None)  # Clear questions
        # Implement any final steps or redirection here

def clear_questions_from_session():
    session.pop('questions', None)
    session.pop('current_question_set', None)
    session.pop('question_index', None)
    session.pop('responses', None)
