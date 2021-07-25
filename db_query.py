# import libraries
from psycopg2 import OperationalError
import pandas as pd

# import files
from data_visualisation import analyse_data


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
        \nEnter anything else to skip.""")
        if choice == '1':
            print('Now exporting...')
            df.to_csv('query_results.csv')
            print('Complete! File name is called query_results.csv')
        elif choice == '2':
            print(f'{df}')
        else:
            print('Skipping.')
        while True:
            print('Would you like to perform some data analysis on your results?')
            print('Type Y for yes or N for no')
            analysis_choice = input().upper()
            if analysis_choice == 'Y':
                analyse_data(df)
                # close connection
                cursor.close()
                break
            elif analysis_choice == 'N':
                print('Returning to the main menu...')
                # close connection
                cursor.close()
                break
            else:
                print('Invalid command - try again!')
    except OperationalError as e:
        print(f"The error {e} occurred!")