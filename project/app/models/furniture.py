from project.app.db import db

class Furniture(db.Model):
    __tablename__  = "furniture"
    furniture_id = db.Column(db.Integer, primary_key = True)
    # room_id = FK
    furniture_type = db.Column(db.String(100), unique = True)
    condition = db.Column(db.String(100))
    # relation between room and furniture
    room_id = db.Column(db.Integer, db.ForeignKey("room.room_id"), nullable = False)
    rooms = db.relationship("Rooms", back_populates = "furniture")