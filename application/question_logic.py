from flask import session
from .models import db, Question

def fetch_and_organize_questions():
    """
    Fetches and organizes questions from the database and stores them in the Flask session.
    """
    # Fetching all questions from the database
    all_questions = {
        'seller': Question.query.filter_by(category='seller').all(),
        'seller_a': Question.query.filter_by(category='seller_a').all(),
        'seller_b': Question.query.filter_by(category='seller_b').all(),
        'seller_c': Question.query.filter_by(category='seller_c').all(),
        'buyer': Question.query.filter_by(category='buyer').all(),
        'car': Question.query.filter_by(category='car').all(),
        'transaction': Question.query.filter_by(category='transaction').all()
    }

    print(all_questions)  # Debugging line
    # Initially, only include the 'seller' questions (excluding the last one)
    organized_questions = {
        'initial': [q.text for q in all_questions['seller'][:-1]]  # Convert Question objects to text
    }

    # Store the organized questions in the session
    session['questions'] = organized_questions
    session['current_question_set'] = 'initial'

def get_next_question_set():
    """
    Retrieves the next set of questions based on user responses and session data.
    Returns None if there are no more questions.
    """
    current_set = session.get('current_question_set', None)
    if current_set is None:
        return None

    questions = session['questions'].get(current_set)

    # Update 'current_question_set' and add additional questions based on user responses
    # Example logic (to be adapted based on actual response handling):
    # if current_set == 'initial':
    #     last_answer = session['responses'].get('last_seller_question', '')
    #     if last_answer == 'titulo del inttt':
    #         session['current_question_set'] = 'seller_a'
    #     elif last_answer == 'documento notariado':
    #         session['current_question_set'] = 'seller_b'
    # ...

    return questions

def store_question_response(question, response):
    """
    Stores the response to a specific question in the session.
    """
    if 'responses' not in session:
        session['responses'] = {}
    session['responses'][question] = response

def clear_questions_from_session():
    """
    Clears the questions and responses from the session.
    """
    session.pop('questions', None)
    session.pop('current_question_set', None)
    session.pop('responses', None)
