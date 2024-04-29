from sql_connection import get_sql_connection


# get all sales
def get_all_sales(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM AutomobileCompany.sales"

    cursor.execute(query)

    response = []

    for (sale_id, vin, dealer_id, customer_id, sale_date, sale_amount) in cursor:
        response.append(
            {
                "sales_id": sale_id,
                'VIN': vin,
                'dealer_id': dealer_id,
                'customer_id': customer_id,
                'sale_date': sale_date,
                'sale_amount': sale_amount
            }
        )

    return response

# inserting new sale information


def insert_new_sale(connection, sale):
    cursor = connection.cursor()
    query = ("INSERT INTO sales"
             "(sale_id, vin, dealer_id, customer_id, sale_date, sale_amount)"
             "VALUES (%s, %s, %s, %s, %s, %s)")
    data = (sale['sale_id'], sale['vin'], sale['dealer_id'], sale['customer_id'], sale['sale_date'], sale['sale_amount'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


# deleting a sale information


def delete_sale(connection, sale_id):
    cursor = connection.cursor()
    query = "DELETE FROM sales WHERE sale_id = %s"
    cursor.execute(query, (sale_id,))
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    sale = {
        'sale_id': '1',
        'vin': '123456H7890K1234G',
        'dealer_id': '1',
        'customer_id': '1',
        'sale_date': '10.10.2002',
        'sale_amount': '10'
    }
    insert_new_sale(connection, sale)

