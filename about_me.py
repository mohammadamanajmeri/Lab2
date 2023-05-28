"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        # TODO: Put full name into data structure
        'full_name': 'Mohammadaman Ajmeri',
        # TODO: Put student ID into data structure
        'Student_Id': 10291830,
        # TODO: Put list of 3 pizza toppings into data structure
        'Pizza_Toppings': [
                'PINEAPPLE',
                'SAUSAGE',
                'PEPPERONI'
        ],
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'avengers:end game',
                'genre': 'sci-fi'
            },
            {
                'title': 'war',
                'genre': 'action'
            }
            # TODO: Add one more movie
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['soylent green', 'racht'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'the lord of the rings', 'fantasy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    first_name = (my_info['full_name'].split())
    first_name = first_name[0]
    print(f"My name is {my_info['full_name']}, but you can call me Sir {first_name}.")
    print(f"My student id is {my_info['Student_Id']}.")

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    # Print bullet list of favourite pizza toppings
    print(f"My favourite pizza toppings are:")
    for toppings in (my_info['Pizza_Toppings']):
        print(f'- {toppings}')

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['Pizza_Toppings'].extend(toppings)
    # Convert all pizza toppings to lowercase
    for i, lowercase_toppings in enumerate(my_info['Pizza_Toppings']):
        my_info['Pizza_Toppings'][i] = lowercase_toppings.lower()
    # Sort toppings list alphabetically
    my_info['Pizza_Toppings'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    new_movie = {
        'title' : 'housefull',
        'genre' : 'comedy'
    }
    my_info['movies'].append(new_movie)
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    movie_genre = [genres['genre'] for genres in my_info['movies']]
    print(f"\n I like to watch {', '.join(movie_genre)} movies")
def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    print()

if __name__ == '__main__':
    main()