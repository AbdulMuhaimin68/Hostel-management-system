from project.app.db import db

class Hostel(db.Model):
    __tablename__ = "hostel"
    hostel_id = db.Column(db.Integer, primary_key = True)
    hostel_name = db.Column(db.String(100))
    hostel_address = db.Column(db.String(500))
    # relation between employees
    employee = db.relationship("Employee", back_populates = "hostel")
    # relation betweeen room and hostel
    rooms = db.relationship("Rooms", back_populates = "hostel")
