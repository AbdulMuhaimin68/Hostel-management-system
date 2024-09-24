from project.app.db import db

class Rooms(db.Model):
    __tablename__ = "room"
    room_id = db.Column(db.Integer, primary_key = True)
    # hostel_id(FK)
    room_type = db.Column(db.String(100))
    room_capacity = db.Column(db.Integer)
    # relation between rooms and hostel
    hostel_id = db.Column(db.Integer, db.ForeignKey("hostel.hostel_id"), nullable = False)
    hostel = db.relationship("Hostel", back_populates = "rooms")
    # relation between rooms and student
    students = db.relationship("Student", back_populates = "rooms")
    # relation between room and furniture
    furniture = db.relationship("Furniture", back_populates = "rooms")