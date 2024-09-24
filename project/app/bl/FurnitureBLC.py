from project.app.repositories.furnitureRepository import FurnitureRepository

class FurnitureBLC:
    
    @staticmethod
    def add_furniture(args:dict):
        session = FurnitureRepository.get_session()
        try:
            result = FurnitureRepository.add_furniture(args, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e