import json

from flask import Flask, jsonify, request
from db import PRODUCTS

app = Flask(__name__)


@app.route('/products/', methods=['GET', 'POST'])
def list_products_handle():
    if request.method == 'GET':
        query = request.args.get('q')
        products_to_show = PRODUCTS
        if query:
            products_to_show = [p for p in PRODUCTS if query.lower() in p['title'].lower()]

        filter_field = request.args.get('filter')
        if filter_field:
            products_to_show = [p for p in products_to_show if p.get(filter_field)]
        return jsonify(products_to_show)
    else:
        raw_product = json.loads(request.data.decode('utf-8'))
        PRODUCTS.append(raw_product)
        return jsonify(raw_product)


if __name__ == '__main__':
    app.run()