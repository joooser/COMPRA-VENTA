from base import FlaskForm, StringField, PasswordField, SubmitField, DataRequired


class LoginForm(FlaskForm):
    username = StringField(label='Nombre de Usuario:', validators=[DataRequired()])
    password = PasswordField(label='Contraseña:', validators=[DataRequired()])
    submit = SubmitField(label='Iniciar Sesión')