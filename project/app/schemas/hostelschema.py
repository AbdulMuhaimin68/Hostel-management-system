from flask_marshmallow import Marshmallow, Schema
from marshmallow import validates, fields, ValidationError
from project.app.models.hostel import Hostel
from flask import Flask
from project.app.schemas.employeeschema import EmployeeSchema

class HostelSchema(Schema):
    class Meta:
        model = Hostel
    #     load_instance = True
    hostel_id = fields.Int(dump_only = True)
    hostel_name = fields.String(required = True)
    hostel_address = fields.String(required = True)
    
    
class PostHostelSchema(HostelSchema):
    pass
class GetHostelSchemaById(Schema):
    hostel_id = fields.Int(required = True)
class UpdateHostelSchema(HostelSchema):
    pass
class DeleteHostelSchema(HostelSchema):
    pass

class GetHostelEmployeeSchema(HostelSchema):
    
    employee = fields.Nested(EmployeeSchema, many=True)

    
    
    