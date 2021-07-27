# import files
from config_db import create_connection
from config_db import db_info
from db_query import db_query

# TODO Investigate sending the data of a query to Tableau


# main method
def main():
    """
    The main method of the program
    """
    print('Welcome to Postgres Toolbox!')
    connection = create_connection()
    db_dict = connection.info.dsn_parameters
    print(f"Now connected to {db_dict['dbname']} as {db_dict['user']}")

    while True:
        print('Main Menu - enter the characters between the brackets to access the desired function')
        print(f"(Query) {db_dict['dbname']}")
        print(f"(Info) on {db_dict['dbname']}")
        print(f"(Exit) program and close connection to {db_dict['dbname']}")

        # get menu choice from user
        menu_choice = input('Enter menu choice - ')

        if menu_choice == 'Query':
            db_query(connection)
        elif menu_choice == 'Info':
            db_info(db_dict)
        elif menu_choice == 'Exit':
            print('Goodbye!')
            connection.close()
            break
        else:
            print(f"I don't understand {menu_choice} - please try again!")


# main entry point to program
if __name__ == '__main__':
    main()
