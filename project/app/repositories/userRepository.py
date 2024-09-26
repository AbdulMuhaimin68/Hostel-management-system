from project.app.models.user import User
from project.app.db import db
from sqlalchemy.orm import scoped_session

class UserRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_user(args:dict, session:scoped_session):
        try:
            user = User(user_name = args['user_name'])
            user.set_password(args['password'])
            session.add(user)
            session.flush()
            return user
        except Exception as e:
            session.rollback()
            raise e
        
