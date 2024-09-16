from app.extensions import db


class ProductAttributes(db.Model):
    __tablename__ = 'product_attributes'
    __table_args__ = {"schema": "dev"}

    attribute_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    variant_id = db.Column(db.Integer, db.ForeignKey('dev.product_variants.variant_id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(255), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    variant = db.relationship('ProductVariants', backref='variant_attributes', foreign_keys=[variant_id])
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updater")
    updater = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")

    def __repr__(self):
        return f'<ProductAttribute {self.name} : {self.value}>'

    def to_dict(self):
        return {
            "attribute_id": self.attribute_id,
            "name": self.name,
            "value": self.value,
        }
