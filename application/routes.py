from application import app
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Role, Subscription, Vehicle, Contractor, PropertyTitle, PropertyDocument, Document
from .forms import LoginForm, RegisterForm, QuestionForm
from .transform_answers import transform_document
from .create_pdf import create_pdf
from .extensions import db, bcrypt
from .question_logic import (initialize_question_session, fetch_questions, 
                             handle_question_response, has_more_questions, 
                             advance_to_next_set, clear_questions_from_session)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter((User.username == form.username.data) |
                                 (User.email == form.username.data)).first()
        if attempted_user and bcrypt.check_password_hash(attempted_user.password_hash, form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home_page'))
        else:
            flash('Inicio de sesión fallido. Por favor, comprueba tu nombre de usuario y contraseña', 'danger')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
        user_to_create = User(username=form.username.data,
                              name=form.name.data,
                              lastname=form.lastname.data,
                              email=form.email.data,
                              password_hash=hashed_password)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Registro exitoso! Has iniciado sesion como {user_to_create.username}", category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'Hubo un error creando el usuario: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/home')
@login_required
def home_page():
    # Aquí puedes agregar lógica para mostrar información relevante en el home
    return render_template('home.html')

@app.route('/logout')
def logout_page():
    logout_user()
    flash("Has cerrado sesión con éxito", 'info')
    return redirect(url_for('login_page'))

@app.route('/create_document', methods=['GET', 'POST'])
@login_required
def create_document():
    if 'questions' not in session:
        initialize_question_session()
        fetch_questions('seller')  # Start with the first set

    if request.method == 'POST':
        response = request.form.get('response')
        handle_question_response(response)

        if not has_more_questions():
            advance_to_next_set()

        return redirect(url_for('create_document'))

    current_questions = session.get('questions', [])
    question_index = session.get('question_index', 0)
    if len(current_questions) > 0:
        current_question = current_questions[question_index]
        return render_template('questions.html', question=current_question, question_index=question_index)
    else:
        clear_questions_from_session()
        # Redirect to a final page or handle the end of the process
        return redirect(url_for('generated_document.html'))  # Replace with the actual final page

@app.route('/generate_document')
@login_required
def generate_document():
    # Logic for generating the document goes here
    return render_template('generated_document.html')


# Añade cualquier otra ruta que necesites aquí

# No es necesario que incluyas if __name__ == '__main__': aquí,
# ya que este archivo se importará en __init__.py y no se ejecutará directamente.