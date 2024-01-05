from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from application.variables import (questions_seller, questions_seller_a, questions_seller_b, questions_seller_c, 
                       questions_buyer, questions_car, questions_transaction, documento)
from application.transform_answers import transform_document
from application.create_pdf import create_pdf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'some_random_key'

db = SQLAlchemy(app)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    # Add your login logic here
    # Example: if form.validate_on_submit(): 
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = LoginForm()
    # Your registration logic here
    return render_template('register.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    session['responses'] = {}
    session.modified = True
    return redirect(url_for('login_page'))

@app.route('/questions/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    all_questions = questions_seller + questions_seller_a + questions_seller_b + questions_seller_c + questions_buyer + questions_car + questions_transaction

    if question_id >= len(all_questions):
        return redirect(url_for('generate_document'))

    current_question = all_questions[question_id]

    if request.method == 'POST':
        answer = request.form.get('answer')
        session['responses'][current_question] = answer
        session.modified = True
        next_question_id = question_id + 1

        if next_question_id < len(all_questions):
            return redirect(url_for('question', question_id=next_question_id))
        return redirect(url_for('generate_document'))

    return render_template('question.html', question=current_question, question_id=question_id)

@app.route('/generate_document')
def generate_document():
    documento_final = transform_document(session['responses'], documento)
    output_pdf = "output.pdf"
    create_pdf(documento_final, output_pdf)
    return render_template('success.html', pdf_file=output_pdf)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')