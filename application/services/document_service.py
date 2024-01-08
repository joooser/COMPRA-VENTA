class DocumentService:
    def __init__(self, db):
        self.db = db

    def create_document(self, user_id, document_data):
        # Get template text
        template_text = self.get_template_text()
        
        # Fill template with user data
        filled_template = self.fill_template(template_text, document_data)
        
        # Save filled template to database
        document = Document(user_id=user_id, content=filled_template)
        self.db.session.add(document)
        self.db.session.commit()

        return document

    def get_document(self, document_id):
        return Document.query.get(document_id)

    def generate_pdf(self, document):
        # Render HTML template 
        html = render_template('pdf.html', content=document.content)
        
        # Convert to PDF
        pdf = pdfkit.from_string(html, False)
        
        return pdf
