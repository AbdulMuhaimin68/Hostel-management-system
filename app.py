from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:smartforum123@localhost/hms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db = SQLAlchemy(app)

class Hostel(db.Model):
    hostel_id = db.Column(db.Integer, primary_key = True)
    hostel_name = db.Column(db.String(100))
    hostel_address = db.Column(db.String(500))
    # relation between employees
    employee = db.relationship("Employee", back_populates = "hostel")
    # relation betweeen room and hostel
    rooms = db.relationship("Rooms", back_populates = "hostel")
    

class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key = True)
    emp_name = db.Column(db.String(100))
    emp_email = db.Column(db.String(150), unique = True)
    emp_phone = db.Column(db.String(15), unique = True)
    emp_role = db.Column(db.String(100),unique = True)
    # relation between room and hostel
    hostel_id = db.Column(db.Integer, db.ForeignKey("Hostel.hostel_id"),nullable = False)
    hostel = db.relationship("Hostel", back_populates = "employee")
    
class Rooms(db.Model):
    room_id = db.Column(db.Integer, primary_key = True)
    # hostel_id(FK)
    room_type = db.Column(db.String(100))
    room_capacity = db.Column(db.Integer)
    # relation between rooms and hostel
    hostel_id = db.Column(db.Integer, db.ForeignKey("Hostel.hostel_id"), nullable = False)
    hostel = db.relationship("Hostel", back_populates = "rooms")
    # relation between rooms and student
    student = db.relationship("Student", back_populates = "rooms")
    # relation between room and furniture
    furniture = db.relationship("Furniture", back_populates = "rooms")
    
    
class Student(db.Model):
    student_id = db.Column(db.Integer , primary_key = True)
    Student_name = db.Column(db.String(100))
    student_email = db.Column(db.String(100), unique = True)
    student_phone = db.Column(db.String(15), unique = True)
    # relation between rooms and student one to many
    room_id = db.Column(db.Integer, db.ForeignKey("Rooms.room_id"), nullable = False)
    rooms = db.relationship("Rooms", back_populates = "students")
    # relation between student and fee
    fees = db.relationship("Fee", back_populates = "student")
    
    
    
class Furniture(db.Model):
    furniture_id = db.Column(db.Integer, primary_key = True)
    # room_id = FK
    furniture_type = db.Column(db.String(100), unique = True)
    condition = db.Column(db.String(100))
    # relation between room and furniture
    room_id = db.Column(db.Integer, db.ForeignKey("Rooms.room_id"), nullable = False)
    rooms = db.relationship("Rooms", back_populates = "furniture")

class Fee(db.Model):
    fee_id = db.Column(db.Integer, primary_key = True)
    # room_id = FK
    # student_id = FK   
    amount = db.Column(db.Integer) 
    # relation between student and fee
    student_id = db.Column(db.Integer, db.ForeignKey("Student.student_id"), nullable = False)
    student = db.relationship("Student", back_populates = "fees")
    

    
with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)
