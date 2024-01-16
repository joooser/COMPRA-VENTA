import traceback

# Extensions
from application.extensions.extensions import db

# Logger
from application.utils.Logger import Logger

# Models
from application.models import Question


def get_questions_grouped_by_category():
    try:

        questions = db.session.query(Question).all()
        questions_by_category = {}
        for question in questions:
            category = question.category
            questions_by_category.setdefault(category, []).append(question)
        return questions_by_category
    
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())