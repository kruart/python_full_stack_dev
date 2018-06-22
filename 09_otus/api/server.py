import json

from flask import Flask, jsonify, request
from db import PRODUCTS, API_KEYS
from marshmallow import Schema, fields

app = Flask(__name__)


class ProductSchema(Schema):
    title = fields.Str(required=True)
    price_uah = fields.Integer(required=True)
    product_image = fields.Str(required=False)
    in_store = fields.Boolean(default=False)


@app.route('/products/', methods=['GET', 'POST'])
def list_products_handle():
    api_key = request.headers.get('HTTP-X-API-KEY')
    if api_key not in API_KEYS:
        response = jsonify({'error': 'Wrong API key'})
        response.status_code = 400
        return response
    if request.method == 'GET':
        query = request.args.get('q')
        products_to_show = PRODUCTS
        if query:
            products_to_show = [p for p in PRODUCTS if query.lower() in p['title'].lower()]

        filter_field = request.args.get('filter')
        if filter_field:
            products_to_show = [p for p in products_to_show if p.get(filter_field)]

        from_element = request.args.get('from')
        to_element = request.args.get('to')
        if from_element and to_element or from_element == 0:
            from_element = int(from_element)
            to_element = int(to_element)
            products_to_show = products_to_show[from_element:to_element]

        fields = request.args.get('fields')
        if fields:
            fields = fields.split(',')
            products_to_show = [{k: v for k, v in p.items() if k in fields} for p in products_to_show]

        return jsonify(products_to_show)
    else:
        raw_product = json.loads(request.data.decode('utf-8'))
        clean_product, errors = ProductSchema().load(raw_product)
        if errors:
            response = jsonify(errors)
            response.status_code = 400
            return response

        else:
            PRODUCTS.append(clean_product)
            return jsonify(raw_product)


if __name__ == '__main__':
    app.run()