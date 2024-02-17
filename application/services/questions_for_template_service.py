from application.models import Questions
from flask import current_app as app

def fetch_questions_by_ids(ids):
    try:
        if not ids:
            return []

        questions = Questions.query.filter(Questions.id.in_(ids)).all()
        return questions
    except Exception as e:
        app.logger.error(f"Error fetching questions by IDs: {e}")
        app.logger.error(f"IDs that caused the error: {ids}")
        return []
