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
        
    @staticmethod
    def update_student_by_id(args: dict):
        session = StudentRepository.get_session()
        try:
            student_id = args.get("student_id")
            if not student_id:
                return jsonify({"message": "student_id not provided"}), 400
            
            # Retrieve the student object by ID
            student = StudentRepository.get_student_by_id(student_id)
            if not student:
                return jsonify({"message": "Student not found"}), 404
            
            # Update student with fields from args
            updated_student = StudentRepository.updated_student(student, args)
            session.commit()
            return updated_student
        except Exception as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_student_by_id(args:dict):
        session = StudentRepository.get_session()
        try:
            result = StudentRepository.delete_student_by_id(args,session)
            session.commit()
            return result
        except Exception as e:
            raise e

            
    