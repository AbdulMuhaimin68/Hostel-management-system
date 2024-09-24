from project.app.models.furniture import Furniture
from project.app.db import db
from sqlalchemy.orm import scoped_session

class FurnitureRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_furniture(args:dict, session:scoped_session):
        try:
            
            furniture = Furniture(**args)
            session.add(furniture)
            session.flush()
            return furniture
        except Exception as e:
            session.rollback()
            raise e
    