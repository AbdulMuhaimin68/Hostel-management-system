from project.app.repositories.feerepository import FeeRepository

class FeeBLC:
    
    @staticmethod
    def add_fee(args:dict):
        session = FeeRepository.get_session()
        try:
            result = FeeRepository.add_fee(args, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e