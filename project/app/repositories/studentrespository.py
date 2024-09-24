from project.app.models.student import Student
from project.app.db import db
from sqlalchemy.orm import scoped_session

class StudentRepository:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_student(args : dict, session:scoped_session):
        try:
            student = Student(**args)
            session.add(student)
            session.flush()
            return student
        except Exception as e:
            session.rollback()
            raise e
            
