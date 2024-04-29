from sql_connection import get_sql_connection


# get all vehicles
def get_all_vehicles(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM AutomobileCompany.vehicles"

    cursor.execute(query)

    response = []

    for (vin, brand_id, model_id, body_style, color, engine, transmission) in cursor:
        response.append(
            {
                'VIN': vin,
                'brand': brand_id,
                'model': model_id,
                'bodyStyle': body_style,
                'color': color,
                'engine': engine,
                'transmission': transmission
            }
        )

    return response


# get all brand information


def get_all_brands(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM AutomobileCompany.brands"

    cursor.execute(query)

    response = []

    for (brand_id, brand_name) in cursor:
        response.append(
            {
                'brand': brand_id,
                'brandName': brand_name,
            }
        )

    return response


# get all model information


def get_all_models(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM AutomobileCompany.models"

    cursor.execute(query)

    response = []

    for (model_id, brand_id, model_name) in cursor:
        response.append(
            {
                'model': model_id,
                'brand': brand_id,
                'modelName': model_name
            }
        )

    return response


def get_brand_id(connection, brand_name):
    cursor = connection.cursor()
    query = "SELECT brand_id FROM brands WHERE brand_name = %s"
    cursor.execute(query, (brand_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None


def get_model_id(connection, model_name):
    cursor = connection.cursor()
    query = "SELECT model_id FROM models WHERE model_name = %s"
    cursor.execute(query, (model_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None


# inserting new vehicle information
def insert_new_products(connection, vehicle):
    cursor = connection.cursor()
    query = ("INSERT INTO vehicles "
             "(vin, brand_id, model_id, body_style, color, engine, transmission)"
             "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    data = (vehicle['vin'], vehicle['brand_id'], vehicle['model_id'], vehicle['body_style'],
            vehicle['color'], vehicle['engine'], vehicle['transmission'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


# deleting new vehicle information


def delete_product(connection, vin):
    cursor = connection.cursor()
    query = "DELETE FROM vehicles WHERE vin = %s"
    cursor.execute(query, (vin,))
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_models(connection))
