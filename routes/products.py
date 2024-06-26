from flask import render_template, request, redirect, url_for
from database.database import db
from models.models import Product
from routes import products_bp


# Create
@products_bp.route('/product/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        barcode = request.form['barcode']
        quantity = request.form['quantity']

        new_product = Product(name=name, description=description, price=price, barcode=barcode, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('get_all_products'))
    return render_template('create_product.html')


# Read - Get all products
@products_bp.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    print("test" + products)
    return render_template('products.html', products=products)


# Update
@products_bp.route('/product/update/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = request.form['price']
        product.barcode = request.form['barcode']
        product.quantity = request.form['quantity']
        db.session.commit()
        return redirect(url_for('get_all_products'))
    return render_template('update_product.html', product=product)


# Delete
@products_bp.route('/product/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('get_all_products'))

