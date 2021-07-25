# import files
from config_db import create_connection
from db_query import db_query


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


# main entry point to program
if __name__ == '__main__':
    main()
