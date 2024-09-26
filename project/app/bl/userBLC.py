from project.app.repositories.userRepository import UserRepository
from flask import jsonify
from project.app.schemas.userschema import UserSchema

class UserBLC:
    
    @staticmethod
    def add_user(args:dict):
        session = UserRepository.get_session()
        try:
            user = UserRepository.add_user(args, session)
            session.commit()
            userchema = UserSchema()
            result = userchema.dump(user)
            return result
        except Exception as e:
            raise e
        