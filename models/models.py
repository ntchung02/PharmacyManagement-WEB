# In models.py
from database.database import db
from sqlalchemy.orm import relationship


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    barcode = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    order_details = relationship('OrderDetail', backref='product', lazy=True)


class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalAmount = db.Column(db.Float)
    paymentMethod = db.Column(db.String(20))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    order_details = relationship('OrderDetail', backref='order', lazy=True)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(10))

    orders = relationship('Order', backref='customer', lazy=True)