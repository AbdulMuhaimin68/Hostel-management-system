from flask import Blueprint, request, jsonify
from webargs.flaskparser import use_args
from marshmallow import fields
from project.app.models.employee import Employee
from project.app.schemas.employeeschema import GetEmployeeSchema, PostEmployeeSchema, PutEmployeeSchema,DeleteEmployeeSchema
from project.app.db import db
import json
from project.app.bl.EmployeeBLC import EmployeeBLC
from http import HTTPStatus


bp = Blueprint("employee", __name__)

@bp.route("/employee", methods=["POST"])
@use_args(PostEmployeeSchema(), location="json")
def create_employee(args):
    try:
        res = EmployeeBLC.add_employee(args)
        emp_schema = PostEmployeeSchema()
        result = emp_schema.dump(res)
        return jsonify({"message": "Employee successfully created", "result": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 422
 

@bp.route("/employee", methods = ["PUT"])
@use_args(PutEmployeeSchema(), location='json')
def update_employee(args):
    try:
        result = EmployeeBLC.update_employee(args)
        employee_schema = PutEmployeeSchema()
        res = employee_schema.dump(result)
        return jsonify({"message" : "data updated successfully!", "result" : res})
    except Exception as e:
        return jsonify({"error" : str(e)}), 422


@bp.route("/get_single_employee", methods = ["GET"])
@use_args({"id":fields.Integer(required=True)},location="query")
def get_single_employee(args):
    try:
        res = EmployeeBLC.get_employe_by_id(args)
        schema= GetEmployeeSchema()
        result = schema.dump(res)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/employee", methods = ["DELETE"])
@use_args(DeleteEmployeeSchema(), location="json")
def Del_employee(args):
    try:
        result = EmployeeBLC.delete_empoloyee_by_id(args)
        print(result)
        return (jsonify({"message": f"employee {args['emp_id']} is deleted successfully"}),HTTPStatus.OK)
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY
    