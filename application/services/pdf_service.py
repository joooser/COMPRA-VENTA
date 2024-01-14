from flask import request
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_new_pdf():
    """
    Creates a PDF file from the text provided in the request JSON.
    Saves the PDF in the current working directory.
    """
    try:
        # Extract data from request
        data = request.json

        # Extract document text
        document_text = data['documentText']

        # Define the PDF file name
        pdf_file_name = "document.pdf"

        # Set up the canvas for the PDF
        c = canvas.Canvas(pdf_file_name, pagesize=letter)
        width, height = letter

        # Add text to the PDF
        c.drawString(100, height - 100, document_text)

        # Save the PDF
        c.save()

        # Confirmation message
        print(f"PDF created successfully: {os.path.abspath(pdf_file_name)}")

    except KeyError:
        print("Error: 'documentText' not found in request.")
    except Exception as e:
        print(f"An error occurred: {e}")
