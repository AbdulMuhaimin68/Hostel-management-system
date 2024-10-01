from project.app.models.furniture import Furniture
from marshmallow import Schema, fields, validate, pre_load, post_load, validates, ValidationError

class FurnitureSchema(Schema):
    class Meta:
        model = Furniture
        
    furniture_id = fields.Integer(dump_only = True)
    furniture_type = fields.String(required=True)
    condition = fields.String(required=True)
    room_id = fields.Integer(required = True)
    
class PostFurniture(Furniture):
    pass

class GetFurnitureSchema(Schema):
    furniture_id = fields.Integer(required = True)
    