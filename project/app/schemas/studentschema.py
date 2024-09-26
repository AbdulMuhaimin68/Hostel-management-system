from flask import Flask
from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields, validate, ValidationError
from project.app.schemas.feeSchema import FeeSchema
from project.app.models.student import Student

class StudentSchema(Schema):
    class Meta:
        model = Student
        
    student_id = fields.Int(dump_only = True)
    student_name = fields.String(required = True)
    student_email = fields.Email(required = True)
    student_phone = fields.String(required=True)
    room_id = fields.Integer(required = True)
    # fee = fields.Nested(FeeSchema, many=True) fee in pending
    
class postStudentSchema(StudentSchema):
    # student_id = fields.Int(required = True)
    pass

class GetStudentSchema(Schema):
    # Fields for filtering or querying data can be optional
    student_id = fields.Int(dump_only=True)
    student_name = fields.String()
    student_email = fields.Email()
    student_phone = fields.String()
    room_id = fields.Integer()
    