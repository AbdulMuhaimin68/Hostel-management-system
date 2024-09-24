from project.app.schemas.furnitureschema import FurnitureSchema
from webargs.flaskparser import use_args
from flask import Blueprint, jsonify
from project.app.bl.FurnitureBLC import FurnitureBLC
from marshmallow import fields
from http import HTTPStatus

bp = Blueprint("furniture", __name__)

@bp.route("/furniture", methods = ["POST"])
@use_args(FurnitureSchema(), location="json")
def add_furniture(args):
    try:
        res = FurnitureBLC.add_furniture(args)
        schema = FurnitureSchema()
        result = schema.dump(res)
        return jsonify({"message" : "furniture added successfully", "result" : result}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"message" : "furniture not added", "error" : str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY
    