import json
import re

from flask import Blueprint, jsonify, render_template, render_template_string, request
from flask import current_app as app
from flask_login import login_required
from markupsafe import escape
from sqlalchemy.exc import SQLAlchemyError

<<<<<<< Updated upstream
from application import db
from application.forms import VehicleSaleForm
from application.models import DocumentType, SubDocumentType, PaymentTypeDocument, Resulting_Document

from application.services.get_document_template_service import get_document_template
from application.services.get_questions_for_template_service import fetch_questions_by_ids
#from application.services.create_pdf_service import generate_pdf
#from application.services.store_pdf_service import store_pdf
=======
from contract_app import db
from contract_app.models import DocumentType, PaymentTypeDocument, SubDocumentType
from contract_app.services.get_document_template_service import get_document_template
from contract_app.services.get_questions_for_template_service import (
    fetch_questions_by_ids,
)

main_blueprint = Blueprint("main", __name__)
>>>>>>> Stashed changes


@main_blueprint.errorhandler(SQLAlchemyError)
def handle_database_errors(error):
    app.logger.error(f"Database error: {error}")
    return jsonify(success=False, error="A database error occurred"), 500


@main_blueprint.route("/", methods=["GET", "POST"])
def landing():
    return render_template("landing.html", title="Landing")


@main_blueprint.route("/home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", title="Home")


@main_blueprint.route("/prices", methods=["GET", "POST"])
def prices():
    return render_template("prices.html", title="prices")


@main_blueprint.route("/create-document", methods=["GET"])
@login_required
def create_document():
    form = VehicleSaleForm()
    try:
<<<<<<< Updated upstream
        questions_by_category = get_questions_grouped_by_category()
=======
        document_types = DocumentType.query.all()
        return render_template("test.html", document_types=document_types)
>>>>>>> Stashed changes
    except SQLAlchemyError as e:
        app.logger.error(f"Error fetching questions: {e}")
        return jsonify(success=False, error=str(e)), 500
    return render_template('create_document.html', form=form, questions_by_category=questions_by_category)


@main_blueprint.route("/test", methods=["GET", "POST"])
@login_required
def test():
    try:
        document_types = DocumentType.query.all()
        return render_template("test.html", document_types=document_types)
    except SQLAlchemyError as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify(success=False, error=str(e)), 500


@main_blueprint.route("/get_sub_document_types", methods=["GET"])
@login_required
def get_sub_document_types():
    document_type_id = request.args.get("documentType")
    try:
        sub_document_types = SubDocumentType.query.filter_by(
            document_type_id=document_type_id
        ).all()
    except SQLAlchemyError as e:
        app.logger.error(f"Error fetching sub document types: {e}")
        return jsonify(success=False, error=str(e)), 500

    options_html = '<option value="">Sub-Documento</option>'
    options_html += "".join(
        [f'<option value="{sub.id}">{sub.name}</option>' for sub in sub_document_types]
    )

    return f"""<select class="form-control" 
                      id="subDocumentType" 
                      name="subDocumentType"
                      hx-get="/get_payment_types"
                      hx-target="#paymentTypeDiv"
                      hx-trigger="change">
                      {options_html}
                </select>"""


@main_blueprint.route("/get_payment_types", methods=["GET"])
@login_required
def get_payment_types():
    try:
        payment_types = PaymentTypeDocument.query.all()
    except SQLAlchemyError as e:
        app.logger.error(f"Error fetching payment types: {e}")
        return jsonify(success=False, error=str(e)), 500

    options_html = '<option value="">Pago en que se reliza la Compra-Venta</option>'
    options_html += "".join(
        [
            f'<option value="{escape(payment.id)}">{escape(payment.name)}</option>'
            for payment in payment_types
        ]
    )

    return f"""<select class="form-control" 
                        id="paymentType" 
                        name="paymentType">
                        {options_html}
                    </select>"""


@main_blueprint.route("/submit_document", methods=["POST"])
@login_required
def submit_document():
    try:
        document_type_id = request.form.get("documentType")
        sub_document_type_id = request.form.get("subDocumentType")
        payment_type_id = request.form.get("paymentType")

        template = get_document_template(
            document_type_id, sub_document_type_id, payment_type_id
        )

        if not template:
            raise ValueError("No template found for the given criteria.")

        document_template_id = template.id
        document_template_id = template.id
        template_text = template.template_text

        placeholder_ids = re.findall(r"data-placeholder=['\"](\d+)['\"]", template_text)
        placeholder_ids = list(set([int(id_) for id_ in placeholder_ids]))

        questions = fetch_questions_by_ids(placeholder_ids)

        template_text_html = f"""<div id="templateDisplay" 
            data-template-id="{document_template_id}" 
            data-type-id="{document_type_id}" 
            class="template-display shadow-lg rounded" 
            hx-swap-oob="true">{template_text}</div>"""

        questions_html = (
            '<form id="questionsContainer" class="justify-content-start mt-5">'
        )
        for question in questions:
            questions_html += f"""
                <div class="question form-group" data-question-id="{question.id}">
                    <p>{question.text}</p>
                    <input type="text" name="answer_{question.id}" data-question-id="{question.id}" class="form-control mb-3">
                </div>
            """
        questions_html += "</form>"

        full_response_html = template_text_html + questions_html
        return render_template_string(full_response_html)
    except Exception as e:
        app.logger.error(f"Error submitting document: {e}")
        return jsonify({"error": str(e)}), 500


@main_blueprint.route("/submit_answers", methods=["POST"])
@login_required
def submit_answers():
    app.logger.info("submit_answers endpoint called")
    data = request.get_json(silent=True)  # Obtener el cuerpo JSON de la solicitud

    try:
        if not data:
            app.logger.error("No data received.")
            return jsonify({"success": False, "message": "No data received."}), 400

        app.logger.info(f"Received JSON data: {json.dumps(data, indent=2)}")
        print(f"Received JSON data: {json.dumps(data, indent=2)}")

        # Aquí iría la lógica para procesar los datos JSON
        # Por ejemplo, extraer información y guardarla en la base de datos

        # Respuesta de éxito
        return jsonify({"success": True, "message": "Answers submitted successfully."})

    except Exception as e:
        app.logger.error(f"Error submitting answers: {e}")
<<<<<<< Updated upstream
        return jsonify(success=False, error=str(e)), 500

#@main_blueprint.route('/paywall')
#@login_required
#def paywall():
#    # Your paywall page logic here...
#    return render_template('paywall.html')
#
#@main_blueprint.route('/serve_pdf/<path:filename>')
#@login_required
#def serve_pdf(filename):
#    # Logic to serve the PDF file...
#    # Same as the existing serve_pdf route from previous suggestions
=======
        db.session.rollback()  # Asegura la idempotencia en caso de error
        return jsonify(
            {
                "success": False,
                "message": "An error occurred while submitting your answers.",
            }
        ), 500
>>>>>>> Stashed changes
