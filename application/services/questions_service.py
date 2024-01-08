from application.extensions import db
from application.models import Question  # Assuming you have a Question model

def get_questions_grouped_by_category():
    questions = db.session.query(Question).all()
    questions_by_category = {}
    for question in questions:
        category = question.category
        questions_by_category.setdefault(category, []).append(question)
    return questions_by_category