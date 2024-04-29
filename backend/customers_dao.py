from sql_connection import get_sql_connection


# get all customer info
def get_all_customers(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM AutomobileCompany.customers"

    cursor.execute(query)

    response = []

    for (customer_id, customer_name, address, phone, gender, annual_income) in cursor:
        response.append(
            {
                'customer': customer_id,
                'customerName': customer_name,
                'address': address,
                'phone': phone,
                'gender': gender,
                'annualIncome': annual_income,
            }
        )

    return response


def insert_new_customers(connection, customer):
    cursor = connection.cursor()
    query = ("INSERT INTO customers "
             "(customer_id, customer_name, address, phone, gender, annual_income)"
             "VALUES (%s, %s, %s, %s, %s, %s)")
    data = (customer['customer_id'], customer['customer_name'], customer['address'], customer['phone'],
            customer['gender'], customer['annual_income'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    customer = {
        'customer_id': '3',
        'customer_name': 'selda',
        'address': '29 Park',
        'phone': '91820344949',
        'gender': 'female',
        'annual_income': '1000000'
    }
    insert_new_customers(connection, customer)

