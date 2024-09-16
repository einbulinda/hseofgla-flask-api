from app import db


class Inventory(db.Model):
    __tablename__ = "inventory"
    __table_args__ = {"schema": "dev"}

    inventory_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    variant_id = db.Column(db.Integer, db.ForeignKey('dev.product_variants.variant_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    warehouse_stock = db.Column(db.Integer, nullable=False, default=0)
    shop_stock = db.Column(db.Integer, nullable=False, default=0)
    reorder_level = db.Column(db.Integer, nullable=False, default=0)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    variant = db.relationship('ProductVariants', backref='inventory_variant', foreign_keys=[variant_id], lazy='joined')
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updater")
    updater = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")

    def __repr__(self):
        return f'<Inventory variant_id: {self.variant_id}, quantity: {self.quantity}>'

    def to_dict(self):
        return {
            "inventory_id": self.inventory_id,
            # "variant_id": self.variant_id,
            "quantity": self.quantity,
            "warehouse_stock": self.warehouse_stock,
            "shop_stock": self.shop_stock,
            "reorder_level": self.reorder_level
        }
