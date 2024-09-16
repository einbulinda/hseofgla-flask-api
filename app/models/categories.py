from app.extensions import db


class Category(db.Model):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'dev'}

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(255), nullable=False)
    parent_category_id = db.Column(db.Integer, db.ForeignKey('dev.categories.category_id'), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_by = db.Column(db.Integer, db.ForeignKey('dev.staff.staff_id'), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=db.func.current_timestamp())

    # Relationships
    parent_category = db.relationship('Category', remote_side=[category_id], backref='subcategories')
    creator = db.relationship('Staff', foreign_keys=[created_by], post_update=True, overlaps="updator")
    updator = db.relationship('Staff', foreign_keys=[updated_by], post_update=True, overlaps="creator")

    def __repr__(self):
        return f'<Category {self.category_name}>'

    def to_dict(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
            "parent_category": self.parent_category.category_name if self.parent_category else None
            # "created_by": self.created_by,
            # "created_date": self.created_date.isoformat(),
            # "updated_by": self.updated_by,
            # "updated_date": self.updated_date.isoformat() if self.updated_date else None
        }
