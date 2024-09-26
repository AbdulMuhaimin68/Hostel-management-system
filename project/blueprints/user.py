from project.app.schemas.userschema import UserSchema, LoginUserSchema
from project.app.bl.LoginBLC import LoginBLC
from project.app.bl.userBLC import UserBLC
from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from werkzeug.security import generate_password_hash
# from werkzeug.security import generate_password_hash
from project.app.models.user import User
from project.app.bl.userBLC import UserBLC
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity, current_user

import uuid

bp = Blueprint("user", __name__)

@bp.route("/register", methods = ["POST"])
@use_args(UserSchema(), location="json")
def register_user(args):
    try:
        if current_user.role != "admin":
            return "admin privileger required" 
        res =UserBLC.add_user(args)
        return jsonify({"message" : "user added successfully", "result" : res}), 201
    except Exception as e:
        return jsonify({"error!" : str(e)})
    
@bp.route("/login", methods = ["POST"])
@use_args(LoginUserSchema(), location="json")
def login(args):
    try:
        res = LoginBLC.login(args)
        return jsonify({"result" : res})
    except Exception as e:
        return jsonify({'error' : str(e)})
    
    