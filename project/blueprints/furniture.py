from project.app.schemas.furnitureschema import FurnitureSchema, GetFurnitureSchema
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
    
@bp.route("/furniture", methods = ["GET"])
@use_args(GetFurnitureSchema(), location="query")
def get_furniture_by_id(args):
    try:
        res = FurnitureBLC.get_furn_by_id(args)
        schema = FurnitureSchema()
        result = schema.dump(res)
        return jsonify({"message" : "furniture data", "result" : result})
    except Exception as e:
        return jsonify({"error", str(e)})
    
@bp.route("/furniture", methods = ["PUT"])
@use_args(GetFurnitureSchema(), location="json")
def update_furniture_by_id(args):
    try:
        res = FurnitureBLC.update_furniture_by_id(args)
        schema = FurnitureSchema()
        result = schema.dump(res)
        return jsonify({"updated data!" : result})
    except Exception as e:
        return jsonify({"error" : str(e)})
        
@bp.route("/furniture", methods=["DELETE"])
@use_args(GetFurnitureSchema(), location="json")
def delete_furniture_by_id(args):
    try:
        res = FurnitureBLC.delete_furniture_by_id(args)

        return jsonify({
            "message": f"furniture {args['furniture_id']} is deleted successfully",
            "result": res
        }), HTTPStatus.OK
    except ValueError as ve:
        return jsonify({"message": str(ve)}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY
