import traceback
import re

# Database
from sqlalchemy.orm import Session

# Logger
from application.utils.Logger import Logger

# Models
from application.models import DocumentTemplate


class ContractService:
    def __init__(self, contract_repository, template_engine):
        self.contract_repository = contract_repository
        self.template_engine = template_engine

    def create_contract(self, contract_data):
        try:
            contract = self.template_engine.render_contract_template(contract_data)
            saved_contract = self.contract_repository.save(contract)
            return saved_contract
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    def get_contract(self, contract_id):
        try:
            contract = self.contract_repository.get_by_id(contract_id)
            return contract
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())


def get_template_text_by_id(template_id: int, db_session: Session):
    try:
        return db_session.query(DocumentTemplate).filter(DocumentTemplate.id == template_id).first()
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

def make_bold_uppercase(match):
    try:
        word = match.group(0)
        return f'<strong>{word[1:-1].upper()}</strong>'
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

def process_template_text(template_text):
    try:
        return re.sub(r'\{([^}]*)\}', make_bold_uppercase, template_text)
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())