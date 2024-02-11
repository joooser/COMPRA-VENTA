from flask import Blueprint, render_template, request, jsonify, current_app as app
from flask_login import login_required
from sqlalchemy.exc import SQLAlchemyError
from markupsafe import escape

from application.services.questions_service import get_questions_grouped_by_category
from application.forms import VehicleSaleForm
from application.services.document_template_service import get_document_template
from application.services.questions_for_template_service import fetch_questions_for_placeholders
from application.models import DocumentType, SubDocumentType, PaymentTypeDocument

# Create a Blueprint for the main routes
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

@main_blueprint.route('/create-document', methods=['GET'])
@login_required
def create_document():
    form = VehicleSaleForm()
    try:
        questions_by_category = get_questions_grouped_by_category()
    except SQLAlchemyError as e:
        app.logger.error(f"Error fetching questions: {e}")
        return jsonify(success=False, error=str(e)), 500
    return render_template('create_document.html', form=form, questions_by_category=questions_by_category)

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

        template_text = get_document_template(document_type_id, sub_document_type_id, payment_type_id)
        if not template_text:
            raise ValueError("No template found for the given criteria.")

        questions = fetch_questions_for_placeholders(template_text)
        if not questions:
            raise ValueError("No questions found for the given template.")

        return render_template('partials/document_and_questions.html', template_text=template_text, questions=questions)
    except Exception as e:
        app.logger.error(f"Error submitting document: {e}")
        return render_template('partials/error.html', error_message=str(e)), 500
