#%%
## Starter Code PART 1

# TODO: Import the necessary modules
import requests

# Keep your Movie class as-is!
class Movie:
    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_movie_title(self):
        return self.movie_data['Title']

    def get_movie_rating(self, source = 'Rotten Tomatoes'):
        for rating in self.movie_data['Ratings']:
            if rating['Source'] == source:
                return(rating['Value'])
        return(f"- Wait - Rating for source {source} was not found!")


# TODO: Create a function, get_api_key(), which reads your API key from your api_key.txt file and returns the clean key
# done
get_api_key = open('/Users/detaer/.omdb.key', 'r')
key = get_api_key.read().rstrip()
get_api_key.close()

base_url = "http://www.omdbapi.com/?"
apikey = f"&apikey={key}"
all_of_it = f"{base_url}{apikey}"

# print(omdb_api_key)
# print(omdb_base_url)
# print(all_of_it)

# TODO: Modify this function to work with your API. Instead of searching through a static list of movie objects,
# have it simply call to the API and return a dictionary object that can be called in the Movie class.
def return_single_movie_object(movie_title):
    """
    Search through list of movie object dictionaries and return the object 
    if the Title of that object matches the movie title passed.

    Parameters:
    * movie_title: str, title of movie whose dict object is to be returned.
    """
    request_url = f"http://www.omdbapi.com/?{apikey}&t={movie_title}"
#    print(request_url)
    response = requests.get(request_url)
    response_data = response.json()
#    print(response_data)
    return(response_data)
# print(return_single_movie_object("back to the future"))


# Keep this function the same. It should work with all your other modified functions, if you created those properly.
def print_single_movie_rating(movie_title):
    """
    Print a movie rating for a given movie.

    Parameters:
    * movie_title: str, title of movie to get rating for.
    """
    this_movie_data = return_single_movie_object(movie_title)
    this_movie_instance = Movie(this_movie_data)
    movie_title = this_movie_instance.get_movie_title()
    movie_rating = this_movie_instance.get_movie_rating()
    print(f"The rating for {movie_title} is {movie_rating}.")
# print_single_movie_rating("Better Off Dead...")

# TODO: Create a function, list_search_results, which searches the API for a movie title and prints out the titles of the 
# movie results
def list_search_results(movie_title):
    request_url = f"http://www.omdbapi.com/?{apikey}&s={movie_title}"
    # print(request_url)
    response = requests.get(request_url)
    response_data = response.json()
#    print(response_data)
#    print(response_data['totalResults'])
    # result_count = response_data[totalResults]
    for each in response_data['Search']:
        print(each['Title'])
    #return(response_data)
# list_search_results("Better Off")

# Keep this function the same - it should take the resulting list from the search function above
def print_all_ratings(movie_list):
    """
    Print a judgement of each movie in a movie list. If the score is over 80,
    print that it's a great movie; if the score is over 60, print that it's a
    good movie; if the score is under 60 print that it's a bad movie.
    
    Parameters:
    * movie_list: list, List of movie titles to print ratings for.
    """
    for movie in movie_list:
        this_movie_data = return_single_movie_object(movie)
        this_movie_instance = Movie(this_movie_data)
        movie_title = this_movie_instance.get_movie_title()
        movie_rating = float(this_movie_instance.get_movie_rating().rstrip("%")) 
        #TODO: Change this to get rid of the "%" at the end of the Rating 
        # #(HINT: % is the last character in the string - How can I get all but the last character?)
        #done
        if movie_rating >= 80:
            print(movie_title, 'is a great movie!')
        elif movie_rating >= 60:
            print(movie_title, 'is a good movie')
        elif movie_rating < 60:
            print(movie_title, 'is a bad movie')

#BONUS: You may see some repeated code in these functions. Consider creating a "base" 
# function that can be used to , and modify the functions accordingly

# 
def main():
    """
    Run from here
    """
    default_movie_list = ['Blade', 'Spirited Away', 'Back to the Future']
    print("\nThanks for using Movie CLI! \n")
    print_all_ratings(default_movie_list)
    print("\n")
    
    while True:
        # TODO: Use "input" to create a prompt that will tell the user to select 1 to search for a movie, 
        # or 2 to find the rating of a specific movie, or 3 to quit
        user_input = int(input("Movie CLI ver. 3.14!\nSelect One:\n1: Search for a movie\n2: Rating of a specific movie\n3: Quit\n: "))

        # TODO: Create an if-elif-else conditional:
        
        # If the user input a "1" above, prompt the user to input a movie title and run list_search_results on the input
        if user_input == 1:
            print("You selected: Search for a movie")
            movie_title = input("Movie Title you would like to search for: ")
            list_search_results(movie_title)
            print("\n")
        # If the user input a "2" above, prompt the user to input a movie titla and run print_single_movie_rating
        elif user_input == 2:
            print("You selected: Rating of a specific movie")
            movie_title_rating = input("Movie title you would like to find the rating of: ")
            print_single_movie_rating(movie_title_rating)
        # If the user input a "3" above, break the while loop (the `break` keyword breaks all loops)
        elif user_input == 3:
            print("You selected: Quit")
            break
        # If the input is not a 1, 2, or 3, print out "You must input a 1, 2, or 3"


if __name__ == '__main__':
    main()