# import libraries
from psycopg2 import OperationalError
import pandas as pd

# import files
from config_db import create_connection


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
        print(f"(Query) {db_info['dbname']}")
        print(f"(Exit) program and close connection to {db_info['dbname']}")

        # get menu choice from user
        menu_choice = input('Enter menu choice - ')

        if menu_choice == 'Query':
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
        # execute query
        cursor.execute(query)
        result = cursor.fetchall()
        # extract the column names
        col_names = []
        for name in cursor.description:
            col_names.append(name[0])
        df = pd.DataFrame(data=result, columns=col_names)
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
        while True:
            print('Would you like to perform some data analysis on your results?')
            print('Type Y for yes or N for no')
            analysis_choice = input().upper()
            if analysis_choice == 'Y':
                analyse_data(df)
            elif analysis_choice == 'N':
                print('Returning to the main menu...')
                break
            else:
                print('Invalid command - try again!')
    except OperationalError as e:
        print(f"The error {e} occurred!")


def analyse_data(data):
    """
    Performs data analysis with Pandas
    :param data: The dataframe created based on the results from the query
    """
    print('Please type in the characters between the brackets.')
    print('(Describe) - perform a variety of mathematics on the generated DataFrame (such as count, mean, etc)')
    print('(Info) - prints the info of the DataFrame. Such as number of rows and columns')
    print('')
    print(data.describe())
    print(data.info)
    print(data.head())


# main entry point to program
if __name__ == '__main__':
    main()
