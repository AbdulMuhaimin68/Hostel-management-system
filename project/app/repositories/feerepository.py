from project.app.models.fee import Fee
from project.app.db import db
from sqlalchemy.orm import scoped_session

class FeeRepository:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_fee(args:dict, session:scoped_session):
        try:
            fee = Fee(**args)
            session.add(fee)
            session.flush()
            return fee
        except Exception as e:
            session.rollback()
            raise e
        