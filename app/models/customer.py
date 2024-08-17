from app.extensions import db
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint


class Customer(db.Model):
    __tablename__ = 'customers'
    __table_args__ = (
        {'schema': 'dev'},
        CheckConstraint('credit_balance >= 0', name='check_credit_balance_non_negative')
    )

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(255), nullable=True, unique=True)
    credit_balance = db.Column(db.Numeric, nullable=False, default=0)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updator")
    updator = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")
    login_details = db.relationship('LoginDetails', backref='customer_account', uselist=False, foreign_keys='LoginDetails.customer_id', overlaps="customer_account")

    def __repr__(self):
        return f'<Customer {self.name}>'

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, "Provided email is invalid."
        return email

    # JSON Serialization
    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "mobile_number": self.mobile_number,
            "email": self.email,
            "credit_balance": float(self.credit_balance),
            "created_by": self.created_by,
            "created_date": self.created_date.isoformat(),
            "updated_by": self.updated_by,
            "updated_date": self.updated_date.isoformat() if self.updated_date else None
        }
