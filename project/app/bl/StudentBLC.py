from project.app.repositories.studentrespository import StudentRepository
from flask import jsonify

class StudentBLC:
    
    @staticmethod
    def add_student(args:dict):
        session = StudentRepository.get_session()
        try:
            result = StudentRepository.add_student(args, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_all_students(args : dict):
        session = StudentRepository.get_session()
        
        try:
            result = StudentRepository.get_all_student(args,session)
            return result
        except Exception as e:
            raise e