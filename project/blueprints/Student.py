from flask import Blueprint, jsonify
from project.app.schemas.studentschema import StudentSchema
from project.app.bl.StudentBLC import StudentBLC
from http import HTTPStatus
from webargs.flaskparser import use_args

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
    
