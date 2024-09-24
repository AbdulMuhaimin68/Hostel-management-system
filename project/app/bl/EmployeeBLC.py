from sqlalchemy.orm import scoped_session
from project.app.repositories.EmployeeRepository import EmployeeRepository
from project.app.db import db
from flask import jsonify

class EmployeeBLC:
    
    @staticmethod
    def add_employee(args: dict):
        session = EmployeeRepository.get_session()
        try:
            result = EmployeeRepository.add_employee(args,session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e

    @staticmethod
    def get_employee_by_id(args: dict):
        id = args.get("id")
        session = EmployeeRepository.get_session()
        result = EmployeeRepository.get_employee_by_id_from_db(id, session)
        if result:
            return result
        else:
            raise Exception("ID not found")
        
    @staticmethod
    def update_employee(args : dict):
        session = EmployeeRepository.get_session()
        
        try:
            employee = EmployeeRepository.geting_employee_by_id_from_db(session, args.get("emp_id"))
            if not employee:
                return jsonify({"error" : "Employee not found"})
            result = EmployeeRepository.update_employee(employee, args)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def delete_empoloyee_by_id(args):
        session = EmployeeRepository.get_session()
        try:
            result = EmployeeRepository.del_emp_by_id(args, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_employee_by_hostel_id(args : dict):
        id = args.get("id")
        session = EmployeeRepository.get_session()
        result = EmployeeRepository.geting_employee_by_id_from_db(session,id)
        if result:
            return result
        else:
            raise Exception("ID not found!")
        
        
        

            
