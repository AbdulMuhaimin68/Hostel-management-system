from webargs.flaskparser import use_args
from project.app.schemas.roomschema import RoomSchema, PostRoomSchema, getAllRooms
from project.app.bl.roomBLC import RoomBLC
from flask import Blueprint, jsonify
from http import HTTPStatus
from project.app.repositories.roomsrepository import RoomsRepository
from project.app.models.rooms import Rooms


bp = Blueprint("room", __name__)

@bp.route("/room", methods = ["POST"])
@use_args(PostRoomSchema(), location="json")
def add_room(args):
    try:
        # breakpoint()
        res = RoomBLC.add_room(args)
        schema = PostRoomSchema()
        result = schema.dump(res)
        return jsonify({"message" : "room created successfully!", "result" : result}), HTTPStatus.OK    
    except Exception as e:
        return jsonify({"message" : "Error creating room", "error" : str(e)}),404
    
@bp.route("/room", methods=["GET"])
@use_args(getAllRooms(), location="json")
def get_all_rooms(args):
    session = RoomsRepository.get_session()
    try:
        res = RoomsRepository.get_all_room(args, session)
        print(res)
        if not res:
            return jsonify({"message": "No rooms found"}), HTTPStatus.NOT_FOUND
        schema = RoomSchema(many=True)
        result = schema.dump(res)
        print(result)
        return jsonify({"message": result}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY
