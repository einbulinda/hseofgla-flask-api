from datetime import datetime
from extensions import db


class Staff(db.Model):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(255), nullable=True, unique=True)
    created_by = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_by = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=datetime.now())

    # Relationships
    creator = db.relationship('Staff', remote_side=[staff_id], foreign_keys=[created_by], post_update=True)
    updator = db.relationship('Staff', remote_side=[staff_id], foreign_keys=[updated_by], post_update=True)

    def __init__(self, name, role, mobile_number=None, email=None, created_by=None):
        self.name = name
        self.role = role
        self.mobile_number = mobile_number
        self.email = email
        self.created_by = created_by

    def __repr__(self):
        return f'<Staff {self.name}>'
