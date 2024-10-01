from project.app.repositories.feerepository import FeeRepository
from flask import Flask, jsonify
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
        
    @staticmethod
    def get_fee_by_id(args:dict):
        session = FeeRepository.get_session()
        try:
            result = FeeRepository.get_fee_by_id(session, id = args.get("fee_id"))
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def update_fee(args:dict):
        session = FeeRepository.get_session()
        try:
            fees_id = FeeRepository.get_fee_by_id(session, args.get("fee_id"))
            if not fees_id:
                return jsonify({"error!": "fee not found"})
            result = FeeRepository.update_fees_data(fees_id, args)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e