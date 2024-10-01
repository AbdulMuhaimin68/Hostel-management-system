from project.app.repositories.furnitureRepository import FurnitureRepository
from project.app.models.furniture import Furniture
from project.app.schemas.furnitureschema  import FurnitureSchema
from flask import Flask, jsonify

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
        
    @staticmethod
    def get_furn_by_id(args:dict):
        session = FurnitureRepository.get_session()
        try:
            result = FurnitureRepository.get_furniture_by_id(session, id = args.get("furniture_id"))
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def update_furniture_by_id(args:dict):
        session = FurnitureRepository.get_session()
        try:
            id = FurnitureRepository.get_furniture_by_id(session, id = args.get("furniture_id"))
            if not id:
                return jsonify({"message" : "id not found"})
            result = FurnitureBLC.update_furniture_by_id(id, args)
            session.commit()
            return result
        except Exception as e:
            raise e
        


    @staticmethod
    def delete_furniture_by_id(args: dict):
        session = FurnitureRepository.get_session()
        try:
            result = FurnitureRepository.delete_furniture(args, session)
            session.commit()
            serialized_result = FurnitureSchema().dump(result)
            
            return serialized_result
        except Exception as e:
            session.rollback()
            raise e

            
            