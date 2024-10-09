from project.app.models.furniture import Furniture
from project.app.db import db
from sqlalchemy.orm import scoped_session
from project.app.models.furniture import Furniture

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
    
    @staticmethod
    def get_furniture_by_id(session:scoped_session, id = None):
        res = session.query(Furniture).filter(Furniture.furniture_id == id).first()
        return res
        
        
    @staticmethod
    def update_furniture(furniture, args:dict):
        furniture.type = args.get("furniture_type", furniture.type)
        furniture.condition = args.get("condition", furniture.condition)
        
        

    @staticmethod
    def delete_furniture(args: dict, session):
        try:
            result = session.query(Furniture).filter(Furniture.furniture_id == args.get("furniture_id")).first()

            # If result is None, raise the ValueError
            if result is None:
                raise ValueError(f"Furniture with id {args.get('furniture_id')} not found.")

            # Proceed with deletion if the object is found
            session.delete(result)
            session.flush()
            return result
        except Exception as e:
            raise e
