import traceback


from application.extensions.extensions import db

from application.utils.Logger import Logger

from application.models import Questions


def get_questions_grouped_by_category():
    try:

        questions = db.session.query(Questions).all()
        questions_by_category = {}
        for question in questions:
            category = question.category
            questions_by_category.setdefault(category, []).append(question)
        return questions_by_category
    
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())