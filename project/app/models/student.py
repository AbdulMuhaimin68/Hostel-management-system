from project.app.db import db 

class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    student_email = db.Column(db.String(100), unique=True, nullable=False)
    student_phone = db.Column(db.String(15), unique=True, nullable=False)

    # Foreign key to the Room model
    room_id = db.Column(db.Integer, db.ForeignKey("room.room_id"), nullable=False)
    rooms = db.relationship("Rooms", back_populates="students")

    # One-to-one relationship with Fee
    fee = db.relationship("Fee", back_populates="student", uselist=False)