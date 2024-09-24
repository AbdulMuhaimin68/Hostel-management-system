from flask import Blueprint, jsonify
from project.app.schemas.feeSchema import FeeSchema
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
    

