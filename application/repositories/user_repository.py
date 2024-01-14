from application.models.models import Document, DocumentTemplate
from application import db

class UserRepository:
    def __init__(self, db):
        self.db = db

    def find_by_username_or_email(self, identifier):
        return User.query.filter((User.username == identifier) | (User.email == identifier)).first()

    def create_user(self, user_data):
        # Get template text
        template_text = DocumentTemplate.query.get(user_data['template_id']).template_text
        
        # Fill in template values
        filled_template = template_text.format(
            buyer_name=user_data['buyer_name'],
            seller_name=user_data['seller_name'],
            car_model=user_data['car_model'],
            sale_price=user_data['sale_price']
        )
        
        # Save filled document
        document = Document(title='Car Sale Contract', text=filled_template)
        db.session.add(document)
        db.session.commit()
        
        return document