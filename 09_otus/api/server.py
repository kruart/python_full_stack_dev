from flask import Flask, jsonify
from db import PRODUCTS

app = Flask(__name__)


@app.route('/list_products/')
def list_products():
    return jsonify(PRODUCTS)


if __name__ == '__main__':
    app.run()