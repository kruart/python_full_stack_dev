import json

from flask import Flask, jsonify, request
from db import PRODUCTS

app = Flask(__name__)


@app.route('/products/', methods=['GET', 'POST'])
def list_products_handle():
    if request.method == 'GET':
        return jsonify(PRODUCTS)
    else:
        raw_product = json.loads(request.data.decode('utf-8'))
        PRODUCTS.append(raw_product)
        return jsonify(raw_product)


if __name__ == '__main__':
    app.run()