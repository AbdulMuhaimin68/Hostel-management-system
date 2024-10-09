from flask import Blueprint, jsonify
from marshmallow import fields
from project.app.schemas.studentschema import StudentSchema, GetStudentSchema, Update_by_id, GetStudentById
from project.app.bl.StudentBLC import StudentBLC
from http import HTTPStatus
from webargs.flaskparser import use_args
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

bp = Blueprint("Student", __name__)

@bp.route("/student", methods = ["POST"])
@use_args(StudentSchema(), location="json")
def add_student(args):
    try:
        res = StudentBLC.add_student(args)
        schema = StudentSchema()
        result = schema.dump(res)
        return jsonify({"messsage" : "Student added successfully!", "result" : result}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error!" : str(e)})
    


@bp.route("/student", methods=["GET"])
@jwt_required()
@use_args(GetStudentSchema(), location='query')
def get_all_student(args):
    try:
        res = StudentBLC.get_all_students(args)
        schema = StudentSchema(many=True)
        result = schema.dump(res)
        return jsonify({"message": "All student data", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/student", methods=["PUT"])
@use_args(Update_by_id(), location="json")
def update_student(args):
    try:
        # Pass `args` as a whole dictionary
        res = StudentBLC.update_student_by_id(args)
        schema = StudentSchema()
        result = schema.dump(res)
        return jsonify({"message": "updated successfully", "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/student", methods=["DELETE"])
@use_args(GetStudentById(), location="json")
def delete_student_by_id(args):
    try:
        res = StudentBLC.delete_student_by_id(args)
        schema = StudentSchema()
        result = schema.dump(res)
        return jsonify({"message" : "student deleted successfully", "result" : result}),201
    except Exception as e:
        return jsonify({"error!" : str(e)})
    
