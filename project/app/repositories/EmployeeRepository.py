from project.app.db import db
from project.app.models.employee import Employee
from sqlalchemy.orm import scoped_session

class EmployeeRepository:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_employee(args: dict, session: scoped_session):
        try:
            employee = Employee(**args)
            session.add(employee)
            session.flush()
            return employee
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_emp_by_id(session, id = None):
        query = session.query(Employee)
        
        if id:
            query.filter(Employee.emp_id == id)
        return query.first()
        
        
    @staticmethod
    def update_employee(employee,args:dict):
        employee.emp_name = args.get("emp_name", employee.emp_name)
        employee.emp_email = args.get("emp_email",  employee.emp_email)
        employee.emp_phone = args.get("emp_phone", employee.emp_phone)
        employee.emp_role = args.get("emp_role", employee.emp_role)
        
        return employee
             
    @staticmethod
    def geting_employee_by_id_from_db(session:scoped_session,id:int,):
        res = session.query(Employee).filter(Employee.emp_id==id).first()
        return res

    @staticmethod
    def del_emp_by_id(args, session):
        try:
            result = session.query(Employee).filter(Employee.emp_id == args.get("emp_id")).first()
            session.delete(result)
            session.flush()
            return result
        except Exception as e:
            session.rollback()
            raise e
