from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    type = db.Column(db.SmallInteger, nullable=False)

    @classmethod
    def login_is_true(cls, username, password):
        user_obj = cls.query.filter_by(username=username).first()
        return user_obj and user_obj.password == password

class SupplyList(db.Model):
    __tablename__ = 'supply_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class LaundryList(db.Model):
    __tablename__ = 'laundry_list'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    queue = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Double, nullable=False)
    pay_status = db.Column(db.SmallInteger)
    amount_tendered = db.Column(db.Double, nullable=False)
    amount_change = db.Column(db.Double, nullable=False)
    remarks = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

class LaundryItems(db.Model):
    __tablename__ = 'laundry_items'
    id = db.Column(db.Integer, primary_key=True)
    laundry_category_id = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Double, nullable=False)
    laundry_id = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Double, nullable=False)
    amount = db.Column(db.Double, nullable=False)

class LaundryCategories(db.Model):
    __tablename__ = 'laundry_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Double, nullable=False)

class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    supply_id = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    stock_type = db.Column(db.SmallInteger, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
