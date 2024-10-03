from project.app.schemas.hostelschema import HostelSchema, PostHostelSchema, GetHostelSchemaById
from project.app.db import db
from project.app.schemas.employeeschema import EmployeeSchema
from project.app.schemas.hostelemployeeSchema import HostelEmployeeSchema,GetHostelEmployeeSchema
from project.app.bl.HostelBLC import HostelBLC
from project.app.bl.EmployeeBLC import EmployeeBLC
from flask import Blueprint, request, jsonify
from webargs.flaskparser import use_args
from marshmallow import fields
from http import HTTPStatus
bp = Blueprint("hostel", __name__)


@bp.route("/hostel", methods = ["POST"])
@use_args(PostHostelSchema(), location="json")
def add_hostel(args):
    try:
        res = HostelBLC.add_hostel(args)
        schema = PostHostelSchema()
        result = schema.dump(res)
        return jsonify({"message": "Hostel successfully created", "result": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 422
    
@bp.route("/hostel", methods = ["GET"])
@use_args({"id" : fields.Int()}, location="query")
def get_hostel_by_id(args):
    try:
        res = HostelBLC.get_hostel_by_id(args)
        schema = HostelSchema()
        result = schema.dump(res)
        return result, HTTPStatus.OK
    
    except Exception as e:
        return jsonify({"Error!" : str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY
    
@bp.route("/hostel/employees", methods = ["GET"])
@use_args({"id" : fields.Int(required = True)}, location="query")
def get_employees_by_id(args):
    try:
        res = HostelBLC.get_hostel_by_id(args)
        schema = GetHostelEmployeeSchema()
        result = schema.dump(res)
        # breakpoint()
        return result, HTTPStatus.OK
    except Exception as e:
        return jsonify({"error!" : str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/hostel", methods=["DELETE"])
@use_args(GetHostelSchemaById(), location="json")
def delete_hostel_by_id(args):
    try:
        res = HostelBLC.delete_hostel_by_id(args)
        
        if res is None:
            # Return an appropriate message if the hostel wasn't found
            return jsonify({"error": "Hostel not found"}), 404
        
        # If deletion was successful, serialize and return the deleted object
        schema = HostelSchema()
        result = schema.dump(res)
        return jsonify({"message": "Data deleted successfully!", "data": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    