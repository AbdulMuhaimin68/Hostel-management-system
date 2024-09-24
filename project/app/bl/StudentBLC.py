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