import json

from flask import Blueprint, render_template, request, jsonify, url_for, flash
from flask_login import login_required, current_user

from application import db

from application.services.questions_service import get_questions_grouped_by_category
from application.services.pdf_service import create_new_pdf
from application.models import Resulting_Document
from application.forms import VehicleSaleForm


# Create a Blueprint for the main routes
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])

@main_blueprint.route('/home', methods=['GET', 'POST'])
@login_required
def home():

    return render_template('home.html', title='Home')

@main_blueprint.route('/create-document', methods=['GET'])
@login_required
def create_document():
    form = VehicleSaleForm()
    questions_by_category = get_questions_grouped_by_category()
    return render_template('create_document.html', form=form, questions_by_category=questions_by_category)

@main_blueprint.route('/test', methods=['GET', 'POST'])
@login_required
def test():

    try:
        form = VehicleSaleForm()

        if form.validate_on_submit():

            answers = request.json

            formData = answers.get('formData', {})
            documentTitle = answers.get('documentTitle', '')
            documentText = answers.get('documentText', '')

            responses_json = json.dumps(formData)

            new_document = Resulting_Document(
                    document=documentText,
                    answers_json=responses_json,
                    user_id=current_user.id
            )

            db.session.add(new_document)
            db.session.commit()

            create_new_pdf()
            flash(f'Success! The Document has been created. And email with the document has been sent.', category='success')

            return jsonify(success=True, redirect=url_for('main.home'))
        
        if form.errors != {}:

            for err_msg in form.errors.values():
                flash(f'Hubo un error creando el usuario: {err_msg}', category='danger')

    except Exception as e:

        print(f"Error processing request: {e}")
        return jsonify(success=False, error=str(e)), 500
    
    return render_template('test.html', form=form)


@main_blueprint.route('/_handle_data', methods=['POST'])
@login_required
def handle_data():
    try:
        if request.method == 'POST':

            answers = request.json

            formData = answers.get('formData', {})
            documentTitle = answers.get('documentTitle', '')
            documentText = answers.get('documentText', '')

            responses_json = json.dumps(formData)
            
            new_document = Resulting_Document(
                title=documentTitle,
                document=documentText,
                answers_json=responses_json,
                user_id=current_user.id
            )

            db.session.add(new_document)
            db.session.commit()

            create_new_pdf()

            flash('Documento creado satisfactoriamente!', 'success')
            return jsonify(success=True, redirect=url_for('main.home'))

    except Exception as e:

        print(f"Error processing request: {e}")
        return jsonify(success=False, error=str(e)), 500