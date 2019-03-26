import json
import pandas as pd

"""
Case of study:
Create a registration system for movies.

It will allow the user:
- Find movies by name, director, year, main actor/actress or list all movies
- Add new movies'register
- Quit of the program
- The data is being stored into a json file
"""


# main function used to call all functionalities considering the argument passed by the user
def start_process():
    user_action = input(
        "\nEnter the action that you would like to do:"
        "\n Enter 'a' to add a movie "
        "\n Enter 'f' to find a movie "
        "\n Enter 'q' to quit: ").lower();

    if user_action == 'a':

        check_addition = add_movie()
        if check_addition:
            print("The movie(s) was(were) inserted as expected!")
        start_process()

    elif user_action == 'f':

        type_reasearch = input(
            "\nEnter how do you want to do the research: "
            "\n Enter 'm' to find by movie name "
            "\n Enter 'd' to find by director name "
            "\n Enter 'y' to find by movie year "
            "\n Enter 'a' to find by main actor/actress "
            "\n Enter '*' to list all movies: ")
        filter_detail = input(
            "\nEnter the filter detail (name of movie, name of director, year movie, main actor/actress or * : ")
        result_research = find_movie(type_reasearch, filter_detail)

        if len(result_research) > 0:

            print("\n")
            print(result_research)
            start_process()

        else:
            print("0 Result. There's no movie registered!")
            start_process()

    elif user_action == 'q':
        print("\nGood bye!")
        exit()

    else:
        start_process()


# Function created to upload the json file to memory
def upload_json_file(name_file):
    # reading each row of the json file and appending it to a list
    json_data = []
    with open(name_file, encoding="utf-8") as file_json:
        for row in file_json:
            json_data.append(json.loads(row))

    return json_data


# Function created to add new registers of movies on the json file
def add_movie():
    name_file = "files/Movies.json"
    add_other_movie = "yes"

    while add_other_movie == "yes":
        # request each information of the new movies and store them on variables
        movie_name = input("\nMovie Name: ")
        director_name = input("Director Name: ")
        movie_year = int(input("Year of the production: "))
        name_main_actor_actress = input("Main actor / Actress: ")

        # create a dictionary variable that will be used to store new movies
        new_movie = {"movie_name": movie_name, "director_name": director_name, "movie_year": movie_year,
                     "name_main_actor_actress": name_main_actor_actress}

        # open the file and add new movies inside it with open('name_file, 'w') as outfile: json.dump(data, outfile)
        file = open(name_file, "a")
        file.write(json.dumps(new_movie) + "\n")
        file.close()

        # check if other movie will be inserted by user
        add_other_movie = input("\nDo you want insert other movie (yes/no): ").lower()

        if add_other_movie == "no":
            return True


# Function created to find movies on the json file considering the parameter passed by user
def find_movie(type_reasearch, filter_detail):
    # name of json file with all Movies created
    name_file = "files/Movies.json"

    # import the file
    file = upload_json_file(name_file)

    # define the lists that will receive the lists of information
    list_movies = []
    list_director = []
    list_year = []
    list_main = []

    # loop that will read each row and create the list to create the dictionary and finally the dataframe
    for row in file:

        # if m (movie_name), then create the lists with information about this row
        if type_reasearch.lower() == "m":
            if row["movie_name"].lower() == filter_detail.lower():
                list_movies.append(row["movie_name"])
                list_director.append(row["director_name"])
                list_year.append(row["movie_year"])
                list_main.append(row["name_main_actor_actress"])

        # if d (director), then create the lists with information about this row
        elif type_reasearch.lower() == "d":
            if row["director_name"].lower() == filter_detail.lower():
                list_movies.append(row["movie_name"])
                list_director.append(row["director_name"])
                list_year.append(row["movie_year"])
                list_main.append(row["name_main_actor_actress"])

        # if y (movie_year), then create the lists with information about this row
        elif type_reasearch.lower() == "y":
            if int(row["movie_year"]) == int(filter_detail):
                list_movies.append(row["movie_name"])
                list_director.append(row["director_name"])
                list_year.append(row["movie_year"])
                list_main.append(row["name_main_actor_actress"])

        # if a (main_actor_actress), then create the lists with information about this row
        elif type_reasearch.lower() == "a":
            if row["name_main_actor_actress"].lower() == filter_detail.lower():
                list_movies.append(row["movie_name"])
                list_director.append(row["director_name"])
                list_year.append(row["movie_year"])
                list_main.append(row["name_main_actor_actress"])

        # else create the lists with information about everything
        else:
            list_movies.append(row["movie_name"])
            list_director.append(row["director_name"])
            list_year.append(row["movie_year"])
            list_main.append(row["name_main_actor_actress"])

    # create the dictionary containing the filter aplied
    dict_movies_filter = {
        "movie_name": list_movies,
        "director_name": list_director,
        "year": list_year,
        "main_actor": list_main
    }

    # create the dataframe with the dictionary values
    df_movies = pd.DataFrame(dict_movies_filter)

    # return the dataframe with the movies filtered
    return df_movies


# Call the main function
start_process()
