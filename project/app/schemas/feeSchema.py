from project.app.models.fee import Fee
from flask_marshmallow import Schema
from marshmallow import validate , fields, ValidationError
from project.app.models.fee import Fee

class FeeSchema(Schema):
    class Meta:
        model = Fee
    fee_id = fields.Int(dump_only = True)
    amount = fields.Int(required = True)
    student_id = fields.Int(required = True)
    
    
class PostFee(FeeSchema):
    # fee_id = fields.Int(required = True)
    pass
    
