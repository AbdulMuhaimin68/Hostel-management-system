from project.app.repositories.roomsrepository import RoomsRepository

class RoomBLC:
    
    @staticmethod
    def add_room(args:dict):
        session = RoomsRepository.get_session()
        try:
            result = RoomsRepository.add_rooms(args, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e