from flask_marshmallow import Marshmallow, Schema
from marshmallow import validates, fields,validate
from project.app.schemas.studentschema import StudentSchema
from project.app.models.rooms import Rooms



class RoomSchema(Schema):
    class Meta:
        model = Rooms
    room_id = fields.Integer(dump_only = True)
    room_type = fields.String(required=True)
    room_capacity = fields.Integer(required = True)
    hostel_id = fields.Integer(required  =True,validates = validate.Range(min=1,error="hostel_id must be a positive integer"))
    # students = fields.Nested(StudentSchema, many=True)
    # furniture = fields.Nested()
    
    
    
class PostRoomSchema(RoomSchema):
    pass
class getAllRooms(Schema):
    # Make all fields optional for a GET request
    hostel_id = fields.Integer(required=False)  # If you want to filter by hostel_id
    room_id = fields.Integer(required=False)
    room_type = fields.String(required=False)
    room_capacity = fields.Integer(required=False)

