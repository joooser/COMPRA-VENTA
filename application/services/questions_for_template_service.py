import re
from application.models import Questions
from flask import current_app as app

def fetch_questions_for_placeholders(template_text):
    try:
        placeholder_pattern = re.compile(r'<span data-placeholder="(\d+)">')
        placeholder_ids = placeholder_pattern.findall(template_text)

        placeholder_ids = [int(id) for id in placeholder_ids]
        questions = Questions.query.filter(Questions.id.in_(placeholder_ids)).order_by(Questions.id).all()

        return questions
    except Exception as e:
        app.logger.error(f"Error fetching questions for placeholders: {e}")
        raise