from project.app.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename___ = "user"
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    role = db.Column(db.String(20), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    