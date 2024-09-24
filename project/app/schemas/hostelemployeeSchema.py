from flask import Flask
from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields, validate, ValidationError
from project.app.models.employee import Employee
from project.app.models.hostel import Hostel
from project.app.schemas.employeeschema import EmployeeSchema
# from project.api import ma
# app = Flask(__name__)
# ma = Marshmallow(app)



# Schema for Employee
class HostelEmployeeSchema(Schema):
    emp_name = fields.String(required=True, validate=validate.Length(min=5, max=50))
    emp_email = fields.Email(required=True)
    emp_phone = fields.String(required=True)
    emp_role = fields.String(required=True)

# Schema for fetching a hostel and its employees
class GetHostelEmployeeSchema(HostelEmployeeSchema):
    hostel_id = fields.Int(required=True)  # Include hostel_id to identify the hostel
    hostel_name = fields.String(required=True)  # Optionally include hostel_name
    employee = fields.Nested(EmployeeSchema, many=True)  # Nested employees schema

    
        