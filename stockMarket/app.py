
import app_arch
from flask import Flask, request, jsonify, abort


app = Flask(__name__)


@app.route('/stock', methods=['GET'])
def market_list():
    return jsonify(app_arch.Stock_market.get_companies())


@app.route('/stock/<string:company_name>', methods=['GET'])
def market_get_company(company_name):
    return jsonify(app_arch.Stock_market.get_company(company_name))


@app.route('/stock/<string:company_name>', methods=['DELETE'])
def market_delete_company(company_name):
    return jsonify(app_arch.Stock_market.delete_company(company_name))


@app.route('/stock', methods=['POST'])
def market_add_company():
    data = request.get_json()
    if data:
        ky = data.keys()
        if 'name' in ky and 'price' in ky:
            return jsonify(app_arch.Stock_market.add_company(data['name'], data['price']))

    abort(400)


@app.route('/stock', methods=['PUT'])
def market_update_company():
    data = request.get_json()
    if data:
        ky = data.keys()
        if 'name' in ky and 'price' in ky:
            return jsonify(app_arch.Stock_market.update_company(data['name'], data['price']))

    abort(400)


# run the app
app.run(debug=True)
