from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
from flask import Flask, render_template


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='should always be secret',

    # Database settings:
    SQLALCHEMY_DATABASE_URI='sqlite:///products.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

    WTF_CSRF_ENABLED=False
)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)

    def __str__(self):
        return("<Product id - {}>".format(self.id))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.desciption
        }


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/products/<id>')
def product_by_id(id):
    product = Product.query.get(id)
    return render_template('product.html', product=product)


if __name__ == '__main__':
    db.create_all()

    # Deleting all records:
    Product.query.delete()

    # Creating new ones:
    product1 = Product(name='product1', description='Cool')
    product2 = Product(name='product2', description='Norm')
    product3 = Product(name='product3', description='No bad')
    product4 = Product(name='product4', description='Bad')

    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.commit()  # note

    # Running app:
    app.run(debug=True)