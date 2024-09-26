from project.app.repositories.loginRepository import LoginRepository
from sqlalchemy.orm import scoped_session

class LoginBLC:
    
    @staticmethod
    def login(args:dict):
        session = LoginRepository.get_session()
        
        try:
            result = LoginRepository.login(args, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e