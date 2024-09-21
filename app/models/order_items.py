from app.extensions import db


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    __table_args__ = {'schema': 'dev'}

    order_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('dev.orders.order_id'), nullable=True)
    variant_id = db.Column(db.Integer, db.ForeignKey('dev.product_variants.variant_id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    discount_rate = db.Column(db.Numeric, default=0)
    discount_amount = db.Column(db.Numeric, default=0)
    price_at_purchase = db.Column(db.Numeric, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    variant = db.relationship('ProductVariants', backref='order_items')
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updater")
    updater = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")

    def __repr__(self):
        return f'<Order Items {self.order_item_id}, Variant: {self.variant_id}, Quantity: {self.quantity}>'

    def to_dict(self):
        return {
            'order_item_id': self.order_item_id,
            'order_id': self.order_id,
            'variant_id': self.variant_id,
            'quantity': self.quantity,
            'discount_rate': float(self.discount_rate),
            'discount_amount': float(self.discount_amount),
            'price_at_purchase': float(self.price_at_purchase),
            'created_by': self.created_by,
            'created_date': self.created_date.isoformat(),
            'updated_by': self.updated_by,
            'updated_date': self.updated_date.isoformat() if self.updated_date else None
        }
