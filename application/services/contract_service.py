# contract_service.py
from application.models import DocumentTemplate
from sqlalchemy.orm import Session
import re

class ContractService:
    def __init__(self, contract_repository, template_engine):
        self.contract_repository = contract_repository
        self.template_engine = template_engine

    def create_contract(self, contract_data):
        # Logic to create a contract from the provided data
        contract = self.template_engine.render_contract_template(contract_data)
        saved_contract = self.contract_repository.save(contract)
        return saved_contract

    def get_contract(self, contract_id):
        # Logic to retrieve a contract by its ID
        contract = self.contract_repository.get_by_id(contract_id)
        return contract


def get_template_text_by_id(template_id: int, db_session: Session):
    return db_session.query(DocumentTemplate).filter(DocumentTemplate.id == template_id).first()

def make_bold_uppercase(match):
    word = match.group(0)
    return f'<strong>{word[1:-1].upper()}</strong>'

def process_template_text(template_text):
    return re.sub(r'\{([^}]*)\}', make_bold_uppercase, template_text)

