from sql_connection import get_sql_connection


# get all dealers
def get_all_dealers(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM AutomobileCompany.dealers"

    cursor.execute(query)

    response = []

    for (dealer_id, dealer_name, location) in cursor:
        response.append(
            {
                'dealer': dealer_id,
                'dealerName': dealer_name,
                'location': location
            }
        )

    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_dealers(connection))
