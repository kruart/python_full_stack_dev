import json

from flask import Flask, jsonify, request
from db import PRODUCTS

app = Flask(__name__)


@app.route('/list_products/')
def list_products_handle():
    return jsonify(PRODUCTS)


@app.route('/add_product/', methods=['POST'])
def add_product_handle():
    raw_product = json.loads(request.data.decode('utf-8'))
    PRODUCTS.append(raw_product)
    return jsonify(raw_product)


if __name__ == '__main__':
    app.run()