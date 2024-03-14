import re

from flask import Blueprint, render_template, request, jsonify, current_app as app, render_template_string, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from markupsafe import escape

from application import db
from application.models import DocumentType, SubDocumentType, PaymentTypeDocument, Resulting_Document

from application.services.get_document_template_service import get_document_template
from application.services.get_questions_for_template_service import fetch_questions_by_ids


main_blueprint = Blueprint('main', __name__)

@main_blueprint.errorhandler(SQLAlchemyError)
def handle_database_errors(error):
    app.logger.error(f'Database error: {error}')
    return jsonify(success=False, error='A database error occurred'), 500

@main_blueprint.route('/', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html', title='Landing')

@main_blueprint.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', title='Home')

@main_blueprint.route('/prices', methods=['GET', 'POST'])
def prices():
    return render_template('prices.html', title='prices')

@main_blueprint.route('/create-document', methods=['GET'])
@login_required
def create_document():
    try:
        document_types = DocumentType.query.all()
        return render_template('test.html', document_types=document_types)
    except SQLAlchemyError as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify(success=False, error=str(e)), 500

@main_blueprint.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    try:
        document_types = DocumentType.query.all()
        return render_template('test.html', document_types=document_types)
    except SQLAlchemyError as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify(success=False, error=str(e)), 500

@main_blueprint.route('/get_sub_document_types', methods=['GET'])
@login_required
def get_sub_document_types():
    document_type_id = request.args.get('documentType')
    try:
        sub_document_types = SubDocumentType.query.filter_by(document_type_id=document_type_id).all()
    except SQLAlchemyError as e:
        app.logger.error(f"Error fetching sub document types: {e}")
        return jsonify(success=False, error=str(e)), 500
    
    options_html = '<option value="">Sub-Documento</option>'
    options_html += ''.join([f'<option value="{sub.id}">{sub.name}</option>' for sub in sub_document_types])
    
    return f'''<select class="form-control" 
                      id="subDocumentType" 
                      name="subDocumentType"
                      hx-get="/get_payment_types"
                      hx-target="#paymentTypeDiv"
                      hx-trigger="change">
                      {options_html}
                </select>'''

@main_blueprint.route('/get_payment_types', methods=['GET'])
@login_required
def get_payment_types():
    try:
        payment_types = PaymentTypeDocument.query.all()
    except SQLAlchemyError as e:
        app.logger.error(f"Error fetching payment types: {e}")
        return jsonify(success=False, error=str(e)), 500

    options_html = '<option value="">Pago en que se reliza la Compra-Venta</option>'
    options_html += ''.join([f'<option value="{escape(payment.id)}">{escape(payment.name)}</option>' for payment in payment_types])
    
    return f'''<select class="form-control" 
                        id="paymentType" 
                        name="paymentType">
                        {options_html}
                    </select>'''

@main_blueprint.route('/submit_document', methods=['POST'])
@login_required
def submit_document():
    try:
        document_type_id = request.form.get('documentType')
        sub_document_type_id = request.form.get('subDocumentType')
        payment_type_id = request.form.get('paymentType')

        template = get_document_template(document_type_id, sub_document_type_id, payment_type_id)

        if not template:
            raise ValueError("No template found for the given criteria.")
        
        document_template_id = template.id
        document_template_id = template.id
        template_text = template.template_text

        placeholder_ids = re.findall(r"data-placeholder=['\"](\d+)['\"]", template_text)
        placeholder_ids = list(set([int(id_) for id_ in placeholder_ids]))

        questions = fetch_questions_by_ids(placeholder_ids)

        template_text_html = f'''<div id="templateDisplay" 
            data-template-id="{document_template_id}" 
            data-type-id="{document_type_id}" 
            class="template-display shadow-lg rounded" 
            hx-swap-oob="true">{template_text}</div>'''

        questions_html = '<form id="questionsContainer" class="justify-content-start mt-5">'
        for question in questions:
            questions_html += f'''
                <div class="question form-group" data-question-id="{question.id}">
                    <p>{question.text}</p>
                    <input type="text" name="answer_{question.id}" data-question-id="{question.id}" class="form-control mb-3">
                </div>
            '''
        questions_html += '</form>'
        
        full_response_html = template_text_html + questions_html
        return render_template_string(full_response_html)
    except Exception as e:
        app.logger.error(f"Error submitting document: {e}")
        return jsonify({'error': str(e)}), 500

@main_blueprint.route('/submit_answers', methods=['POST'])
@login_required
def submit_answers():
    app.logger.info('submit_answers endpoint called')

    if not request.form.get('answers_json'):
        return jsonify({'success': False, 'message': 'Answers data is required.'}), 400

    try:
        answers_json = request.form.get('answers_json')
        plain_text = request.form.get('plain_text')
        document_template_id = request.form.get('document_template_id')
        document_type_id = request.form.get('document_type_id')

        if answers_json and plain_text and document_template_id and document_type_id:
            # All required data is present, proceed to save
            new_resulting_document = Resulting_Document(
                answers_json=answers_json,
                plain_text=plain_text,
                user_id=current_user.id,
                document_type_id=document_type_id,
                document_template_id=document_template_id
            )
            db.session.add(new_resulting_document)
            db.session.commit()

        # Redirect based on subscription status
        if current_user.subscription_id == 1:
            # User is subscribed, generate PDF
            pdf_relative_path = generate_pdf_and_store(plain_text, new_resulting_document.id)
            download_url = url_for('serve_pdf', filename=pdf_relative_path)
            message = "Document saved successfully. Your download will begin shortly."

            return jsonify({
                'success': True,
                'message': message,
                'redirect_url': url_for('home'),
                'pdf_download_url': url_for('serve_pdf', filename=pdf_relative_path)
            })
        
        else:

            message = "Document saved successfully. Please subscribe to download as a PDF."

            return jsonify({
                'success': True,
                'message': message,
                'redirect_url': url_for('paywall'),

            })

    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error submitting answers: {e}")
        return jsonify(success=False, error=str(e)), 500