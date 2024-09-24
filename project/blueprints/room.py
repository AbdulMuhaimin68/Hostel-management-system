from webargs.flaskparser import use_args
from project.app.schemas.roomschema import PostRoomSchema
from project.app.bl.roomBLC import RoomBLC
from flask import Blueprint, jsonify
from http import HTTPStatus

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