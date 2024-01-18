from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, validators, SelectField, IntegerField, DateField, TextAreaField, FloatField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError, InputRequired
from application.models import User