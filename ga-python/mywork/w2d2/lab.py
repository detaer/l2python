movie_title = "Back to the Future"
Movie_Rating = 8

print('The rating for', movie_title, 'is', Movie_Rating)

# 1. A `list` of movies that includes Back to the Future, Blade, and Spirited Away. Later, we will be using an API to pull a huge list of movies, but for now we will just pretend it only has these three.
List_Of_Movies = ["Back to the Future", "Blade", "Spirited Away"]

# 1. A variable called `movie_rating` with a value of `8`. Later, we will be using an API to pull the ratings to a lot of movies, but for now we are going to hard-code every movie rating to `8`.
Movie_Rating = 8

# 1. A function that, when called, will list all available movies. So, at this point, it will be listing the three movies we hard-coded above.
def Print_Movie_List():
    for movie in List_Of_Movies:
        print(movie)

# 1. A function that, when called with the name of a movie as its `argument`, will tell the user whether or not that movie is available (i.e. if that movie is in your list of movies).
def Movie_In_List(Is_It_In):
    Movie_In_Stock = False
    for Movie in List_Of_Movies:
        if Movie == Is_It_In:
            Movie_In_Stock = True
    if Movie_In_Stock == True:
        print(Is_It_In,"is in stock.")
        return Movie_In_Stock
    else:
        print(Is_It_In,"is not in stock.")
        return Movie_In_Stock

# Movie_In_List("Singing in the rain")
# Movie_In_List("Blade")

# 1. A function that, when called with the name of a movie as its `argument`, will tell the user the rating of that movie (at this point, it will always be `8`, 
# but remember that eventually the value for `movie_rating` will change, so make sure your code reflects that). If the movie is not available (i.e. not in your list), 
# the function will tell the user that the rating is unavailable.
def What_Is_The_Rating(Movie_Want_rating):
    if Movie_In_List(Movie_Want_rating) == False:
        print("Error - Movie is not in our list of movies")
        return "Unknown Movie"
    else:
        print(Movie_Want_rating, "has a rating of",  Movie_Rating, ".")

# What_Is_The_Rating("Brundle")
# What_Is_The_Rating("Blade")

# 1. A function that allows you to pass a `list` as an `argument` which will print out whether each movie in the list has a "great" rating (8 or more),
#  a "good" rating (6 or more), a "bad" rating (less than 6), or no rating (i.e. the movie is unavailable).
def How_Are_These_Movies(Questionable_Movies):
    for Movie in Questionable_Movies:
        if Movie_In_List(Movie) == False:
            return "Unknown movie"
        if Movie_Rating >= 8:
            print(Movie, "is great!")
        elif Movie_Rating >= 6:
            print(Movie, "is good.")
        elif Movie_Rating < 6:
            print(Movie, "we don't like that movie so much.")

Gimmie_Reviews = ["Blade", "Brundle"]
How_Are_These_Movies(Questionable_Movies = Gimmie_Reviews)



# 1. Some code that tests each function (think of the possible inputs that a user could put in, and make sure the output of each function is as expected).
# 1. Meaningful comments and variable names.
# 1. BONUS: Think of some ways to deal with the fact that users may not correctly capitalize the movie name.
# If they type in `back to the future` instead of `Back to the Future`, what will happen? How can you fix that? Once you think *conceptually* of the solution,
# search Google to see if you can find out how to do it in Python.