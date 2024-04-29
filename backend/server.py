from flask import Flask, request, jsonify
from flask_cors import CORS
from sql_connection import get_sql_connection
import products_dao, customers_dao, dealers_dao, sales_dao

app = Flask(__name__)
CORS(app)
connection = get_sql_connection()


@app.route('/getVehicles', methods=['GET'])
def get_vehicles():
    vehicles = products_dao.get_all_vehicles(connection)
    return jsonify(vehicles)


@app.route('/getBrands', methods=['GET'])
def get_brands():
    brands = products_dao.get_all_brands(connection)
    return jsonify(brands)


@app.route('/getModels', methods=['GET'])
def get_models():
    models = products_dao.get_all_models(connection)
    return jsonify(models)


@app.route('/insertProducts', methods=['POST'])
def insert_product():
    try:
        product_data = {
            'vin': request.form['vin'],
            'brand': request.form['brand_id'],
            'model': request.form['model_id'],
            'bodyStyle': request.form['body_style'],
            'color': request.form['color'],
            'engine': request.form['engine'],
            'transmission': request.form['transmission']
        }
        return_id = products_dao.insert_new_products(connection, product_data)
        return jsonify({'vin': return_id}), 201  # Return the created resource ID and a 201 Created status
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error message and a 500 Internal Server Error status


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        return_id = products_dao.delete_product(connection, request.form['vin'])
        return jsonify({'vin': return_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/getCustomers', methods=['GET'])
def get_customers():
    try:
        customers = customers_dao.get_all_customers(connection)
        return jsonify(customers), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/insertCustomer', methods=['POST'])
def insert_customer():
    try:
        customer_data = {
            'customer_id': request.form['customer_id'],
            'customer_name': request.form['customer_name'],
            'address': request.form['address'],
            'phone': request.form['phone'],
            'gender': request.form['gender'],
            'annual_income': request.form['annual_income']
        }
        return_id = customers_dao.insert_new_customers(connection, customer_data)
        return jsonify({'customer_id': return_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/getDealers', methods=['GET'])
def get_dealers():
    try:
        dealers = dealers_dao.get_all_dealers(connection)
        return jsonify(dealers), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/getSales', methods=['GET'])
def get_sales():
    try:
        sales = sales_dao.get_all_sales(connection)
        return jsonify(sales), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/insertSale', methods=['POST'])
def insert_sale():
    try:
        sale_data = {
            'sale_id': request.form['sale_id'],
            'vin': request.form['vin'],
            'dealer_id': request.form['dealer_id'],
            'customer_id': request.form['customer_id'],
            'sale_date': request.form['sale_date'],
            'sale_amount': request.form['sale_amount']
        }
        return_id = sales_dao.insert_new_sale(connection, sale_data)
        return jsonify({'sale_id': return_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/deleteSale', methods=['POST'])
def delete_sale():
    try:
        return_id = sales_dao.delete_sale(connection, request.form['sale_id'])
        return jsonify({'sale_id': return_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
