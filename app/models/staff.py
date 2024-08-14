
from datetime import datetime
from app.extensions import db


class Staff(db.Model):
    __tablename__ = 'staff'
    __table_args__ = {'schema': 'dev'}

    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(255), nullable=True, unique=True)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=datetime.now)

    # Relationships
    creator = db.relationship('Staff', remote_side=[staff_id], foreign_keys=[created_by], post_update=True, overlaps="updator")
    updator = db.relationship('Staff', remote_side=[staff_id], foreign_keys=[updated_by], post_update=True, overlaps="creator")
    login_details = db.relationship('LoginDetails', foreign_keys='LoginDetails.staff_id', uselist=False, overlaps="staff_account")

    def __repr__(self):
        return f'<Staff {self.name}>'
