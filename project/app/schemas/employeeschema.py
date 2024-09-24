from flask import Flask
from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields, validate, ValidationError
from project.app.models.employee import Employee
# from project.app.schemas.hostelschema import HostelSchema
app = Flask(__name__)
ma = Marshmallow(app)

class EmployeeSchema(Schema):
    class Meta:
        model = Employee
    emp_id = fields.Int(dump_only=True)
    emp_name = fields.String(required = True, validate = validate.Length(min = 5, max = 50))
    emp_email = fields.Email(required = True)
    emp_phone = fields.String(required = True)
    emp_role = fields.String(required=True)
    hostel_id = fields.Int(required=True)
    
# class employe_hostel(EmployeeSchema):
#     employee = fields.List(fields.Nested(HostelSchema,many=True))
class GetEmployeeSchema(EmployeeSchema):
    pass

class PostEmployeeSchema(EmployeeSchema):
    pass

class PutEmployeeSchema(EmployeeSchema):
    emp_id = fields.Int()
    
class DeleteEmployeeSchema(ma.Schema):
    emp_id = fields.Int(required = True)


