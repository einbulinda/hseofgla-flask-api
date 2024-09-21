from app.extensions import db


class Order(db.Model):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'dev'}

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('dev.customers.customer_id'), nullable=True)
    total_items_count = db.Column(db.Integer, nullable=False)
    total_order_amount = db.Column(db.Numeric, nullable=False)
    order_status = db.Column(db.String(50), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    customer = db.relationship('Customer', backref='orders')
    order_items = db.relationship('OrderItem', backref='order', lazy='dynamic', cascade='all, delete-orphan')
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updater")
    updater = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")

    def __repr__(self):
        return f'<Order {self.order_id}, status: {self.order_status}>'

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'total_items_count': self.total_items_count,
            'total_order_amount': float(self.total_order_amount),
            'order_status': self.order_status,
            'order_date': self.order_date.isoformat(),
            'created_by': self.created_by,
            'created_date': self.created_date.isoformat(),
            'updated_by': self.updated_by,
            'updated_date': self.updated_date.isoformat() if self.updated_date else None,
            'order_items': [item.to_dict() for item in self.order_items]
        }


