from .base import (
    FlaskForm,
    StringField,
    PasswordField,
    SubmitField,
    DataRequired,
    ValidationError,
    Length,
    Email,
    EqualTo,
    User,
    RecaptchaField
    )

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):

        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_to_check):
        
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists! Please try a different email address')

    email     = StringField(label='Correo Electrónico:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Contraseña:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirmar Contraseña:', validators=[EqualTo('password1'), DataRequired()])
    
    #recaptcha = RecaptchaField()
    submit    = SubmitField(label='Crear Cuenta')

class LoginForm(FlaskForm):
    username = StringField(label='Correo Electrónico:', validators=[DataRequired()])
    password = PasswordField(label='Contraseña:', validators=[DataRequired()])
    submit = SubmitField(label='Iniciar Sesión')