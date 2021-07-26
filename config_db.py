# import libraries
import psycopg2
from psycopg2 import OperationalError
import json
import os.path


def create_connection():
    """
    :return: a connection object which can be used to interact with the Postgres DB
    """

    while True:
        if os.path.exists('db_info.json'):
            try:
                print('Found saved login - now reading...')
                # open JSON file and close it
                with open('db_info.json', 'r') as file:
                    db_data = json.load(file)
                    file.close()
                # unpack dictionary
                db_name = db_data['db_name']
                db_user = db_data['db_user']
                db_password = db_data['db_password']
                db_host = db_data['db_host']
                db_port = db_data['db_port']
            except AssertionError as error:
                print(f'An error has occurred!\nError details {error}')

        else:
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
            while True:
                if not os.path.exists('db_info.json'):
                    print('Would you like to save these details for next time?')
                    print('Type Y for yes or N for no.')
                    save_choice = input("Enter command - ").upper()
                    if save_choice == 'Y':
                        save_login(db_name, db_user, db_password, db_host, db_port)
                        return connection
                    elif save_choice == 'N':
                        return connection
                    else:
                        print('Invalid command - try again!')
                else:
                    return connection
        except OperationalError as e:
            # if it fails, throw error
            print(f"The error '{e}' occurred")
            print('Please try again!')


def save_login(db_name, db_user, db_password, db_host, db_port):
    """
    Saves DB login info for next time as a JSON file
    :param db_name: The name of the database
    :param db_user: The username
    :param db_password: The username's password
    :param db_host: The name of the host running Postgres
    :param db_port: The port which the Postgres DB uses
    """
    print("Now saving DB info to JSON file....")
    # create dictionary
    db_dict = {'db_name': db_name, 'db_user': db_user, 'db_password': db_password, 'db_host': db_host, 'db_port': db_port}
    # create json
    json_file = json.dumps(db_dict, indent=4)
    with open("db_info.json", "w") as outfile:
        outfile.write(json_file)
    print('Complete! File saved as db_info.json')


def db_info(db_dict):
    """
    :param db_dict: the connection information to a Postgres DB
    """
    print('Information on connected DB')
    print(f"DB Name - {db_dict['dbname']}")
    print(f"User - {db_dict['user']}")
    print(f"Host - {db_dict['host']}")
    print(f"Port - {db_dict['port']}")
    print(f"SSL Mode - {db_dict['sslmode']}")
    print(f"SSL Compression - {db_dict['sslcompression']}")
    print(f"Minimum SSL Protocol Version - {db_dict['ssl_min_protocol_version']}")
    print('Enter any keys to return to the menu')
    any_key = input('')
