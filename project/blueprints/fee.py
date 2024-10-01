from flask import Blueprint, jsonify
from project.app.schemas.feeSchema import FeeSchema, GetFeeSchema, PutFeeSchema
from project.app.bl.FeeBLC import FeeBLC
from webargs.flaskparser import use_args
from http import HTTPStatus
bp = Blueprint('fee', __name__)

@bp.route("/fee", methods = ["POST"])
@use_args(FeeSchema(), location= "json")
def add_fee(args):
    try:
        res = FeeBLC.add_fee(args)
        schema = FeeSchema()
        result = schema.dump(res)
        return jsonify({"message" : "Fee add successfully!", "result" :result}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"message" : "Error!" , "error" : str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY
    
@bp.route("/fee", methods=["GET"])
@use_args(GetFeeSchema(), location="query")
def get_all_fees(args):
    try:
        # Pass args to the BLC method
        res = FeeBLC.get_fee_by_id(args)
        if res:
            schema = FeeSchema()
            result = schema.dump(res)
            return jsonify({"message": "The fee search by id is", "result": result}), HTTPStatus.OK
        else:
            return jsonify({"message": "No fee found for the given id"}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/fee", methods = ["PUT"])
@use_args(PutFeeSchema(), location="json")
def update_fee(args):
    try:
        res = FeeBLC.update_fee(args)
        schema = FeeSchema()
        result = schema.dump(res)
        return jsonify({"message" : "fee data updated successfully!", "result" : result})
    except Exception as e:
        return jsonify({"error" : str(e)})
    