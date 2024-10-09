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
            
    @staticmethod
    def get_all_student(args:dict, session:scoped_session):
        try:
            student = session.query(Student).all()
            return student
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_student_by_id(student_id):
        try:
            return db.session.query(Student).filter_by(student_id=student_id).first()
        except Exception as e:
            raise e



    @staticmethod
    def updated_student(student,args:dict):
        student.student_name = args.get("student_name", student.student_name)
        student.student_email = args.get("student_email", student.student_email)
        student.student_phone = args.get("student_phone", student.student_phone)
        student.room_id = args.get("room_id", student.room_id)
        
        return student            
            
    @staticmethod
    def delete_student_by_id(args:dict, session:scoped_session):
        try:
            result = session.query(Student).filter(Student.student_id==args.get("student_id")).first()
            if result is None:
                raise ValueError(f"student with id {args.get("student_id")} not found")
            session.delete(result)
            session.flush()
            return result
        except Exception as e:
            raise e
            
