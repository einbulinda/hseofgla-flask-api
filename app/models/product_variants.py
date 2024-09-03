from app.extensions import db


class ProductVariants(db.Model):
    __tablename__ = 'product_variants'
    __table_args__ = {"schema": "dev"}

    variant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('dev.products.product_id'), nullable=False)
    sku = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Numeric, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    product = db.relationship('Product', backref='variants', foreign_keys=[product_id])
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updater")
    updater = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")

    def __repr__(self):
        return f'<ProductVariant SKU: {self.sku}, Price: {self.price}>'

    def to_dict(self):
        return {
            "variant_id": self.variant_id,
            "product_id": self.product_id,
            "sku": self.sku,
            "price": float(self.price),
            "created_by": self.created_by,
            "created_date": self.created_date.isoformat(),
            "updated_by": self.updated_by,
            "updated_date": self.updated_date.isoformat() if self.updated_date else None
        }
