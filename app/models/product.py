from app.extensions import db
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'products'
    __table_args__ = {"schema": "dev"}

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('dev.categories.category_id'), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    category = db.relationship('Category', backref='products', foreign_keys=[category_id])
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updater")
    updater = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")
    variants = db.relationship('ProductVariant', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.product_name}>'

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "category_id": self.category_id,
            "is_active": self.is_active,
            "created_by": self.created_by.isoformat(),
            "created_date": self.created_date.isoformat(),
            "updated_by": self.updated_by,
            "updated_date": self.updated_date.isoformat() if self.updated_date else None
        }

