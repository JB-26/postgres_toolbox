# import libraries
import seaborn as sns
from colorama import init, deinit, Fore, Style

# TODO build functions that visualise distributions of data and plotting categorical data


def analyse_data(data):
    """
    Performs data analysis with Pandas
    :param data: The dataframe created based on the results from the query
    """
    while True:
        print('Please type in the characters between the brackets.')
        print('(Describe) - perform a variety of mathematics on the generated DataFrame (such as count, mean, etc)')
        print('(Info) - prints the info of the DataFrame. Such as number of rows and columns')
        print('(Head) - view the first five rows of the DataFrame')
        print('(Graph) - for visualising the results from the query in a graph')
        print('(Exit) - return to the main menu')
        data_choice = input('Enter your choice - ')
        if data_choice == 'Describe':
            print(data.describe())
        elif data_choice == 'Info':
            print(data.info)
        elif data_choice == 'Head':
            print(data.head())
        elif data_choice == 'Graph':
            build_graph_menu(data)
            break
        elif data_choice == 'Exit':
            print('Returning to the main menu...')
            break
        else:
            print('Invalid command - please try again!')


def build_graph_menu(df):
    """
    Offers the user a range of choices of how to build a graph to visualise data
    :param df: the DataFrame containing the results of the query ran by the user
    """
    while True:
        init()
        print('Welcome to visualising your results!')
        print('This program uses the Seaborn library for data visualisation')
        print('Please enter the number for what type of plot you want to use')
        print('1 - Visualising statistical relationships')
        print('2 - Visualising distributions of data')
        print('3 - Plotting with categorical data')
        print('4 - Return to main menu')
        # warning message
        print(Fore.RED, Style.BRIGHT + 'WARNING! Performance could be impacted when working with large data sets!')
        print(Style.RESET_ALL)
        deinit()

        graph_choice = input('Please enter a number - ')
        if graph_choice == '1':
            vis_stat(df)
        elif graph_choice == '2':
            print('2')
        elif graph_choice == '3':
            print('3')
        elif graph_choice == '4':
            print('Returning to main menu')
            break


def vis_stat(df):
    """
    Visualises statistical data using Seaborn
    :param df: DataFrame for analysis and visualisation
    """
    # set the theme
    sns.set_theme(style="darkgrid")

    while True:
        try:
            # set x and y axis
            print('Please enter the name of the column to be used for the X axis')
            x_axis = input('Enter X axis name - ')
            print('Please enter the name of the column to be used for the Y axis')
            y_axis = input('Enter Y axis name - ')

            # set hue (optional)
            print('Would you like to add a Hue to the graph? (Optional)')
            print('Enter Yes or No.')
            hue_choice = input('Enter input - ')

            if hue_choice == 'Yes':
                print('Enter the name for the Hue')
                hue = input('Enter hue value - ')
                # build graph
                sns.relplot(x=x_axis, y=y_axis, hue=hue, data=df)
                break
            elif hue_choice == 'No':
                # build graph
                sns.relplot(x=x_axis, y=y_axis, data=df)
                break
            else:
                print('Invalid command - try again!')
        except AssertionError as error:
            print('Error!')
            print(f'Error details:\n{error}')


def vis_distribution(df):
    """
    :param df: DataFrame for analysis and visualisation
    Visualises data distribution with Seaborn
    """
    # set the theme
    sns.set_theme(style="darkgrid")
    print('Data distribution')


def vis_categorical(df):
    """
    :param df: DataFrame for analysis and visualisation
    Visualises categorical data
    """
    # set the theme
    sns.set_theme(style="darkgrid")
    print('Categorical data')
