#%%
movie_object_list = [{'Title': 'Back to the Future',
  'Year': '1985',
  'Rated': 'PG',
  'Released': '03 Jul 1985',
  'Runtime': '116 min',
  'Genre': 'Adventure, Comedy, Sci-Fi',
  'Ratings': [{'Source': 'Internet Movie Database', 'Value': '8.5'},
   {'Source': 'Rotten Tomatoes', 'Value': '96'},
   {'Source': 'Metacritic', 'Value': '87'}],
  'Production': 'Universal Pictures'},
 {'Title': 'Spirited Away',
  'Year': '2001',
  'Rated': 'PG',
  'Released': '28 Mar 2003',
  'Runtime': '125 min',
  'Genre': 'Animation, Adventure, Family, Fantasy, Mystery',
  'Ratings': [{'Source': 'Internet Movie Database', 'Value': '8.6'},
   {'Source': 'Rotten Tomatoes', 'Value': '77'},
   {'Source': 'Metacritic', 'Value': '96'}],
  'Production': 'Walt Disney Pictures'},
 {'Title': 'Blade',
  'Year': '1998',
  'Rated': 'R',
  'Released': '21 Aug 1998',
  'Runtime': '120 min',
  'Genre': 'Action, Horror, Sci-Fi',
  'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.1'},
   {'Source': 'Rotten Tomatoes', 'Value': '54'},
   {'Source': 'Metacritic', 'Value': '45'}],
  'Production': 'New Line Cinema'}]


class Movie:

    """
    The Movie class holds all the data for a single movie, has getter methods to get title and movie rating
    """

    def __init__(self, movie_data):
        """
        Store the raw movie data

        Parameters: 
        * movie_data: dict, full dictionary of movie data
        """
        self.movie_data = movie_data

    def get_movie_title(self):
        """
        Return movie title from the raw data.
        """
        return self.movie_data['Title']

    def get_movie_rating(self, source = 'Rotten Tomatoes'):
        """
        Return movie rating given source, 
        
        Paramters:
        source: str, source of desired movie rating. Defaults to Rotten Tomatoes
        """
        for rating in self.movie_data['Ratings']:
            if rating['Source'] == source:
                return(rating['Value'])

        return(f"- Wait - Rating for source {source} was not found!")


def return_single_movie_object(movie_title):
    """
    Search through list of movie object dictionaries and return the object 
    if the Title of that object matches the movie title passed.

    Parameters:
    * movie_title: str, title of movie whose dict object is to be returned.
    """
    for movie_object in movie_object_list:
        if movie_object['Title'] == movie_title:
            return movie_object


def print_single_movie_rating(movie_query):
    """
    Print a movie rating for a given movie.

    Parameters:
    * movie_query: str, title of movie to get rating for.
    """
    this_movie_data = return_single_movie_object(movie_query)
    this_movie_instance = Movie(this_movie_data)
    movie_title = this_movie_instance.get_movie_title()
    movie_rating = this_movie_instance.get_movie_rating()
    print(f"The rating for {movie_title} is {movie_rating}.")


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
        movie_rating = float(this_movie_instance.get_movie_rating())
        if movie_rating >= 80:
            print(movie_title, 'is a great movie!')
        elif movie_rating >= 60:
            print(movie_title, 'is a good movie')
        elif movie_rating < 60:
            print(movie_title, 'is a bad movie')


def main():
    """
    Run from here
    """
    print_all_ratings(['Blade', 'Spirited Away', 'Back to the Future'])
    print_single_movie_rating('Spirited Away')


if __name__ == '__main__':
    main()
