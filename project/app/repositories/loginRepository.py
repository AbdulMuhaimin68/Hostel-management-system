from project.app.models.user import User
from flask_jwt_extended import create_access_token
from project.app.db import db
from datetime import timedelta

class LoginRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def login(args, session):
        user_name = args.get('user_name')
        password = args.get('password')

        user = session.query(User).filter(User.user_name == user_name).first()
        if not user or not user.check_password(password):
            return {'message': 'Invalid username or password'}

        access_token = create_access_token(identity=user_name, expires_delta=timedelta(days=30))
        return access_token