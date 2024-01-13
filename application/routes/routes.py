from application import app, db
from flask import Blueprint, render_template, request, jsonify, url_for, flash
from flask_login import login_required
from application.services.questions_service import get_questions_grouped_by_category
import json
from application.models.models import Resulting_Document

# Create a Blueprint for the main routes
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])

@main_blueprint.route('/home', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('home.html', title='Home')

@main_blueprint.route('/create-document', methods=['GET', 'POST'])
@login_required
def create_document():
    try:
        if request.method == 'POST':
            # Process the form data and save it as needed
            answers = request.get_json()

            # Assuming 'answers' is a dictionary with the form data
            document_title = answers.get('document_title', 'Sin Título')
            responses_json = json.dumps(answers.get('responses', {}))

            # Create a new Resulting_Document instance
            new_document = Resulting_Document(
                title=document_title,
                answers_json=responses_json
            )

            # Add the new document to the session and commit it to save in the database
            db.session.add(new_document)
            db.session.commit()

            # Optionally, flash a success message
            flash('Document created successfully!', 'success')

            # Redirect to the home page
            return jsonify(success=True, redirect=url_for('Home'))

    except Exception as e:
        # Log the exception and return an error response
        print(f"Error processing request: {e}")
        return jsonify(success=False, error=str(e)), 500

    questions_by_category = get_questions_grouped_by_category()

    return render_template('create_document.html', questions_by_category=questions_by_category)

@main_blueprint.route('/test', methods=['GET', 'POST'])
@login_required
def test():

    return render_template('test.html')