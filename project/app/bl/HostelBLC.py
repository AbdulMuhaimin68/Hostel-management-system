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
            