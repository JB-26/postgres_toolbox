# import libraries
import psycopg2
from psycopg2 import OperationalError
import pandas as pd


# main method
def main():
    """
    The main method of the program
    """
    print('Welcome to Postgres Toolbox!')
    connection = create_connection()
    db_info = connection.info.dsn_parameters
    print(f"Now connected to {db_info['dbname']} as {db_info['user']}")

    while True:
        print('Main Menu - enter the characters between the brackets to access the desired function')
        print(f"(Q)uery {db_info['dbname']}")
        print(f"(Exit) program and close connection to {db_info['dbname']}")

        # get menu choice from user
        menu_choice = input('Enter menu choice - ')

        if menu_choice == 'Q':
            db_query(connection)
        elif menu_choice == 'Exit':
            print('Goodbye!')
            connection.close()
            break
        else:
            print(f"I don't understand {menu_choice} - please try again!")


def db_query(connection):
    """
    :param connection: Database connection
    """
    print(f"Query Database - {connection.info.dsn_parameters['dbname']}")
    # Open a cursor to perform database operations
    cursor = connection.cursor()
    print('Enter your query below')
    query = input('')
    print('Now executing...')
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(data=result)
        # drop column which has the row number
        df = df.drop(df.columns[0], axis=1)
        print('Success! Would you like to export the results to a CSV file or view the results?')
        choice = input("""Enter 1 to export to CSV or 2 to view the results.
        \nEnter anything else to return to the main menu.""")
        if choice == '1':
            print('Now exporting...')
            df.to_csv('query_results.csv')
            print('Complete! File name is called query_results.csv')
            # close connection
            cursor.close()
        elif choice == '2':
            print(f'{df}')
            # close connection
            cursor.close()
        else:
            print('Returning to menu!')
            # close connection
            cursor.close()
    except OperationalError as e:
        print(f"The error {e} occurred!")


def create_connection():
    """
    :return: a connection object which can be used to interact with the Postgres DB
    """

    while True:
        # get db info from user
        print('Please enter the following information below.')
        db_name = input('Enter the DB Name - ')
        db_user = input('Enter the user name - ')
        db_password = input('Enter the DB Password - ')
        db_host = input('Enter the host name - ')
        db_port = input('Enter the port - ')

        try:
            # attempt to connect to db
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print(f"\nConnection to PostgreSQL DB successful")
            return connection
        except OperationalError as e:
            # if it fails, throw error
            print(f"The error '{e}' occurred")
            print('Please try again!')


# main entry point to program
if __name__ == '__main__':
    main()
