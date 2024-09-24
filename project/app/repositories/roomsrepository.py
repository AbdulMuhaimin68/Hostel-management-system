from project.app.db import db
from project.app.models.rooms import Rooms
from sqlalchemy.orm import scoped_session

class RoomsRepository:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_rooms(args:dict, session:scoped_session):
        try:
            rooms = Rooms(**args)
            session.add(rooms)
            session.flush()
            return rooms
        except Exception as e:
            session.rollback()
            raise e
        
        