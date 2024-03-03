from weasyprint import HTML
from flask import render_template_string

def generate_pdf_from_template(data):
    # Assuming `data` is a dictionary with the data to render the template
    # Load the HTML template as a string
    with open('app/templates/document.html', 'r') as file:
        html_template = file.read()

    # Render the HTML template with the data
    rendered_html = render_template_string(html_template, **data)

    # Generate the PDF
    pdf = HTML(string=rendered_html).write_pdf()

    return pdf
