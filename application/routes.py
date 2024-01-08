from application import app
from flask import render_template, request, session, jsonify, redirect, url_for
from flask_login import login_required
from application.auth.auth_routes import auth_blueprint
from flask import render_template
from flask_login import login_required
from application.auth.auth_routes import auth_blueprint
from .services.questions_service import get_questions_grouped_by_category
from .services.contract_service import get_template_text_by_id, process_template_text
from .extensions import db


# Register the authentication blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/', methods=['GET', 'POST'])

@app.route('/home')
@login_required
def home():
    # Aquí puedes agregar lógica para mostrar información relevante en el home
    return render_template('home.html', title='Home')

@app.route('/create-document')
@login_required
def create_document():
    template_text = get_template_text_by_id(1, db.session)
    processed_text = process_template_text(template_text.template_text)
    
    if request.method == 'POST':
        # Store the answers in the session for debugging
        session['answers'] = request.form.to_dict()
        print(session['answers'])  # Print the answers to the console for debugging
        return jsonify(success=True)  # You can redirect or respond as needed
    
    questions_by_category = get_questions_grouped_by_category()

    return render_template('create_document.html', processed_text=processed_text, questions_by_category=questions_by_category)
