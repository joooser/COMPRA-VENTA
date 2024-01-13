from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class QuestionForm(FlaskForm):
    answer = StringField('Answer')
    submit = SubmitField('Submit')