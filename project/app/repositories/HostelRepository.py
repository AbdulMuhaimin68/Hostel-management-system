from flask import Flask, jsonify
from project.app.models.hostel import Hostel
from project.app.db import db
from sqlalchemy.orm import scoped_session
# from sqlalchemy import and_

class HostelRepository:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_hostel(args:dict, session:scoped_session):
        try:
            hostel = Hostel(**args)
            session.add(hostel)
            session.flush()
            return hostel
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_hostel_by_id(session: scoped_session, id: int):
        res = session.query(Hostel).filter(Hostel.hostel_id == id).first()
        if res is None:
            return None 
        return res
    



        