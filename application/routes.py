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
                             advance_to_next_set, clear_questions_from_session,
                             CATEGORY_NAMES)
from .document_manager import save_responses_to_db, get_template_and_fill_content
from flask import jsonify

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
        fetch_questions(session['current_question_set'])

    if request.method == 'POST' and 'document_title' in request.form:
        session['document_title'] = request.form['document_title']

        # Redirect to the next step in the document creation process
        next_url = url_for(('create_document'))  # Replace with your actual view function
        return jsonify({'success': True, 'redirect': next_url})

        response = request.form.get('response')
        handle_question_response(response)

        if not has_more_questions():
            advance_to_next_set()

        # Revisar si todas las preguntas de todos los sets han sido respondidas
        if session.get('all_questions_answered', False):
            # Todas las preguntas han sido respondidas, guardar respuestas en la base de datos
            document_id = save_responses_to_db()
            session['document_id'] = document_id
            clear_questions_from_session()
            return redirect(url_for('review_document'))

        return redirect(url_for('create_document'))

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

    # Si no hay más preguntas en el set actual, avanzar al siguiente set
    if not has_more_questions():
        advance_to_next_set()

    return redirect(url_for('create_document'))

@app.route('/review_document', methods=['GET', 'POST'])
@login_required
def review_document():
    document_id = session.get('document_id')
    if not document_id:
        # Si no hay un ID de documento, redirige para comenzar el proceso de nuevo
        return redirect(url_for('create_document'))

    if request.method == 'POST':
        # Aquí manejarías la edición final del documento si es necesario,
        # y luego la creación del PDF
        return redirect(url_for('generate_pdf', document_id=document_id))

    # Obtener el contenido llenado de la plantilla
    filled_content = get_template_and_fill_content(document_id)
    return render_template('review_document.html', content=filled_content, document_id=document_id)

@app.route('/generate_pdf/<int:document_id>', methods=['POST'])
@login_required
def generate_pdf(document_id):
    # Obtener el documento de la base de datos
    document = Document.query.get(document_id)
    if document:
        # Utilizar 'create_pdf' o una función similar para generar el PDF desde 'answers_json'
        pdf = create_pdf(document.answers_json)
        # Aquí asumimos que 'create_pdf' devuelve un objeto de respuesta Flask con el PDF
        return pdf

    flash('Error al generar el PDF.', 'error')
    return redirect(url_for('home_page'))

@app.route('/update_document_preview', methods=['POST'])
@login_required
def update_document_preview():
    # Extract the response from the AJAX request
    response = request.form.get('response', '').upper()  # Convert to uppercase
    # Here, add your logic to update the document based on the response
    # For now, let's assume you return the response as the preview
    preview_html = f"<strong>{response}</strong>"  # Example: make the response bold for the preview
    return jsonify({'previewHtml': preview_html})
