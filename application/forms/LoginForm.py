from .base import FlaskForm, StringField, PasswordField, SubmitField, DataRequired


class LoginForm(FlaskForm):
    email = StringField(label='Email:', validators=[DataRequired()])
    password = PasswordField(label='Contraseña:', validators=[DataRequired()])
    submit = SubmitField(label='Iniciar Sesión')