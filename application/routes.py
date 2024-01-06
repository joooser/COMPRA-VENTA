from application import app
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Role, Subscription, Vehicle, Contractor, PropertyTitle, PropertyDocument, Document
from .forms import LoginForm, RegisterForm
from .variables import (
    questions_seller, questions_seller_a, questions_seller_b, questions_seller_c,
    questions_buyer, questions_car, questions_transaction
)
from .transform_answers import transform_document
from .create_pdf import create_pdf
from .extensions import db

@app.route('/')
@app.route('/home')
def home_page():
    # Aquí puedes agregar lógica para mostrar información relevante en el home
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        # Aquí va la lógica de inicio de sesión
        pass
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # Aquí va la lógica de registro
        pass
    return render_template('register.html', form=form)

@app.route('/questions/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    all_questions = questions_seller + questions_seller_a + questions_seller_b + questions_seller_c + questions_buyer + questions_car + questions_transaction
    if question_id < len(all_questions):
        current_question = all_questions[question_id]
        if request.method == 'POST':
            answer = request.form.get('answer')
            session['responses'][current_question] = answer
            session.modified = True
            next_question_id = question_id + 1
            if next_question_id < len(all_questions):
                return redirect(url_for('question', question_id=next_question_id))
            else:
                return redirect(url_for('generate_document'))
        return render_template('questions.html', question=current_question, question_id=question_id)
    else:
        # Lógica cuando todas las preguntas hayan sido respondidas
        return redirect(url_for('generate_document'))

@app.route('/generate_document')
def generate_document():
    documento_final = transform_document(session['responses'], documento)
    output_pdf = "output.pdf"
    create_pdf(documento_final, output_pdf)
    return render_template('success.html', pdf_file=output_pdf)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

@app.route('/create_task', methods=['POST'])
def create_task():
    # Lógica para crear una nueva tarea
    # ...
    return redirect(url_for('home_page'))


# Añade cualquier otra ruta que necesites aquí

# No es necesario que incluyas if __name__ == '__main__': aquí,
# ya que este archivo se importará en __init__.py y no se ejecutará directamente.