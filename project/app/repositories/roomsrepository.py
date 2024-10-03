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
        
    @staticmethod
    def get_all_room(args: dict, session: scoped_session):
        query = session.query(Rooms)
    
        # Apply filters only if they are present
        if 'room_id' in args:
            query = query.filter(Rooms.room_id == args['room_id'])
        if 'hostel_id' in args:
            query = query.filter(Rooms.hostel_id == args['hostel_id'])
        if 'room_type' in args:
            query = query.filter(Rooms.room_type == args['room_type'])
        if 'room_capacity' in args:
            query = query.filter(Rooms.room_capacity == args['room_capacity'])
        
        res = query.all()  # Fetch all matching records
        print(res)  # Log the result to see if rooms are returned
        
        if not res:
            return None
        
        return res
