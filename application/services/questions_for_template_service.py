import re
from application.models import Questions
from flask import current_app as app

def fetch_questions_by_ids(ids):
    questions = Questions.query.filter(Questions.id.in_(ids)).all()
    return questions