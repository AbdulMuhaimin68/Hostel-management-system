from flask import Blueprint, jsonify
from project.app.schemas.studentschema import StudentSchema, GetStudentSchema
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

    
    
