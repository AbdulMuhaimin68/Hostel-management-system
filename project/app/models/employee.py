from project.app.db import db

class Employee(db.Model):
    __tablename__ = "employee"
    emp_id = db.Column(db.Integer, primary_key = True)
    emp_name = db.Column(db.String(100))
    emp_email = db.Column(db.String(150), unique = True)
    emp_phone = db.Column(db.String(15), unique = True)
    emp_role = db.Column(db.String(100),unique = True)
    # relation between room and hostel
    hostel_id = db.Column(db.Integer, db.ForeignKey("hostel.hostel_id"),nullable = False)
    hostel = db.relationship("Hostel", back_populates = "employee")