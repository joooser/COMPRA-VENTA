from application import app
from flask import render_template, request, jsonify
from flask_login import login_required
from application.auth.auth_routes import auth_blueprint
from .services.questions_service import get_questions_grouped_by_category

# Register the authentication blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/', methods=['GET', 'POST'])

@app.route('/home')
@login_required
def home():
    # Aquí puedes agregar lógica para mostrar información relevante en el home
    return render_template('home.html', title='Home')

@app.route('/create-document', methods=['GET', 'POST'])
@login_required
def create_document():

    if request.method == 'POST':
        # Process the form data and save it as needed
        answers = request.get_json()

        return jsonify(success=True)
    
    questions_by_category = get_questions_grouped_by_category()

    return render_template('create_document.html', questions_by_category=questions_by_category)


@app.route('/questions')
@login_required
def index():
    return render_template('questions.html')


@app.route('/dynamic')
@login_required
def dynamic():

    questions_by_category = get_questions_grouped_by_category()

    return render_template('review_document.html', questions_by_category=questions_by_category)
