from routes import (products_bp)

from flask import Flask, render_template
from database.database import db
from models.models import Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:68686868@localhost/PharmacyManagement?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register blueprints
app.register_blueprint(products_bp)
# app.register_blueprint(customers_bp)
# app.register_blueprint(orders_bp)
# app.register_blueprint(order_details_bp)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
