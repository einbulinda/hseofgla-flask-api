from app.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.customer import Customer


class LoginDetails(db.Model):
    __tablename__ = "login_details"
    __table_args__ = {'schema': 'aud'}

    loggin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=False, unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('dev.customers.customer_id'), nullable=True)
    username = db.Column(db.String(255), nullable=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    failed_attempts = db.Column(db.Integer, nullable=False, default=0)
    is_locked = db.Column(db.Boolean, nullable=False, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    staff = db.relationship('Staff', foreign_keys=[staff_id], overlaps="login_details")
    customer = db.relationship('Customer', foreign_keys=[customer_id], overlaps="customer_account,login_details")
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updator")
    updator = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return{
            "loggin_id": self.loggin_id,
            "staff_id": self.staff_id,
            "customer_id": self.customer_id,
            "username": self.username,
            "failed_attempts": self.failed_attempts,
            "is_locked": self.is_locked
        }

    def __repr__(self):
        return f'<LoginDetails {self.username}>'
