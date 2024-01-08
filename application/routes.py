from application import app
from flask import render_template
from flask_login import login_required
from application.auth.auth_routes import auth_blueprint
from flask import render_template, jsonify, redirect, url_for, request, session
from flask_login import login_required
from application.auth.auth_routes import auth_blueprint


# Register the authentication blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/', methods=['GET', 'POST'])

@app.route('/home')
@login_required
def home():
    # Aquí puedes agregar lógica para mostrar información relevante en el home
    return render_template('home.html', title='Home')

@app.route('/create_document', methods=['GET', 'POST'])
@login_required
def create_document():
    def initialize_question_session():
        # Add your implementation here
        pass

    def fetch_questions(question_set):
        # Add your implementation here
        pass

    if 'questions' not in session:
        initialize_question_session()
        fetch_questions(session['current_question_set'])

    if request.method == 'POST' and 'document_title' in request.form:
        session['document_title'] = request.form['document_title']

        # Redirect to the next step in the document creation process
        next_url = url_for('create_document')  # Replace with your actual view function
        return jsonify({'success': True, 'redirect': next_url})

    current_questions = session.get('questions', [])
    question_index = session.get('question_index', 0)

    if current_questions:
        current_question = current_questions[question_index]
        set_name = session.get('current_set_name', 'Set de Preguntas')
        full_question_label = f"{set_name}: Pregunta {question_index + 1}"
        return render_template('questions.html',
                                question=current_question,
                                question_label=full_question_label,
                                question_index=question_index)

    return redirect(url_for('create_document'))