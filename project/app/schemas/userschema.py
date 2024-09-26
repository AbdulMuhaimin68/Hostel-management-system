from project.app.models.user import User
from flask_marshmallow import Schema
from marshmallow import fields, validates, ValidationError


class UserSchema(Schema):
    class Meta:
        model = User
    user_id = fields.Integer(dump_only = True)
    user_name = fields.String(required = True)
    password = fields.String(required=True)
    role = fields.String(required=True)
    
    @validates('role')
    def validate_role(self, value):
        if value not in ['admin', 'user', 'distributor']:
            raise ValidationError('Invalid role. Roles must be admin, student, or employee.')
    
    
class LoginUserSchema(UserSchema):
    user_name = fields.String(required=True)
    password = fields.String(required = True)