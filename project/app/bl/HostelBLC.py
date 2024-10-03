from project.app.repositories.HostelRepository import HostelRepository
from flask import Flask, jsonify
from project.app.db import db

class HostelBLC:
    
    @staticmethod
    def add_hostel(args:dict):
        session = HostelRepository.get_session()
        try:
            result = HostelRepository.add_hostel(args, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_hostel_by_id(args:dict):
        id = args.get("id")
        session = HostelRepository.get_session()
        result = HostelRepository.get_hostel_by_id(session, id)
        # breakpoint()
        if result:
            return result
        else:
            raise Exception("ID not found!")
        
    @staticmethod
    def delete_hostel_by_id(args: dict):
        session = HostelRepository.get_session()
        try:
            id = args.get("hostel_id")  # Assuming 'id' comes from args
            result = HostelRepository.get_hostel_by_id(session, id)

            if result is None:
                # Return None when hostel is not found
                return None
            
            # Delete the hostel if found
            session.delete(result)
            session.commit()
            return result

        except Exception as e:
            session.rollback()  # Ensure rollback on failure
            raise e

            
            