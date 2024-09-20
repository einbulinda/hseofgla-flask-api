from app.extensions import db


class Discount(db.Model):
    __tablename__ = 'discounts'
    __table_args__ = {'schema': 'dev'}

    discount_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    discount_name = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('dev.products.product_id'), nullable=False)
    variant_id = db.Column(db.Integer, db.ForeignKey('dev.product_variants.variant_id'), nullable=False)
    discount_rate = db.Column(db.Numeric, nullable=False, default=0)
    discount_amount = db.Column(db.Numeric, nullable=False, default=0)
    start_date = db.Column(db.Date, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    product = db.relationship('Product', backref='discounts', lazy=True)
    variant = db.relationship('ProductVariants', backref='variant_discounts', foreign_keys=[variant_id])
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updator")
    updator = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")

    def __repr__(self):
        return f'Discount {self.discount_name}: {self.discount_rate or self.discount_amount}>'

    def to_dict(self):
        return {
            'discount_id': self.discount_id,
            'discount_name': self.discount_name,
            'product_id': self.product_id,
            'variant_id': self.variant_id,
            'discount_rate': float(self.discount_rate) if self.discount_rate else None,
            'discount_amount': float(self.discount_amount) if self.discount_amount else None,
            'start_date': self.start_date.isoformat(),
            'expiry_date': self.expiry_date.isoformat() if self.expiry_date else None,
            'description': self.description,
            'created_by': self.created_by,
            'created_date': self.created_date.isoformat(),
            'updated_by': self.updated_by,
            'updated_date': self.updated_date.isoformat() if self.updated_date else None
        }


# TODO:To update the relationship for discounts on fetching product details. 17/09/2024
