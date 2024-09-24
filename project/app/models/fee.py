from project.app.db import db

class Fee(db.Model):
    __tablename__ = "fee"
    fee_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    # Foreign key to the Student model, ensuring one-to-one relationship
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), unique=True, nullable=False)
    student = db.relationship("Student", back_populates="fee", uselist=False)