from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from .models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists! Please try a different email address')

    name = StringField(label='Nombre:', validators=[DataRequired()])
    lastname = StringField(label='Apellido:', validators=[DataRequired()])
    username = StringField(label='Nombre de Usuario:', validators=[Length(min=3, max=30), DataRequired()])
    email = StringField(label='Correo Electrónico:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Contraseña:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirmar Contraseña:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Crear Cuenta')

class LoginForm(FlaskForm):
    username = StringField(label='Nombre de Usuario:', validators=[DataRequired()])
    password = PasswordField(label='Contraseña:', validators=[DataRequired()])
    submit = SubmitField(label='Iniciar Sesión')

class QuestionForm(FlaskForm):
    answer = StringField('Answer')
    submit = SubmitField('Submit')