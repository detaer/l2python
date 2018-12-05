# My favorite romance movies
# title, release year, runtime, tagline, main characters
romantic_movie1 = ("The Princess Bride", 1987, 98, "The story of a man and a woman who lived happily ever after.", ["Buttercup", "Westley", "Fezzik", "Inigo Montoya", "Vizzini"])
romantic_movie2 = ("Groundhog Day", 1993, 101, "He's having the day of his life… over and over again.", ["Phil Connors"])
romantic_movie3 = ("Amélie", 2001, 122, "One person can change your life forever.", ["Amélie Poulain", "Nino Quincampoix", "The Garden Gnome"])
romantic_movies = (romantic_movie1, romantic_movie2, romantic_movie3)
# expected output
# Here are my favorite romance movies:
# The Princess Bride (1987): The story of a man and a woman who lived happily ever after.
# Groundhog Day (1993): He's having the day of his life...over and over again.
# Amélie (2001): One person can change your life forever.

print("Here are my favorite romance movies:")

for each in romantic_movies:
    print(f"{each[0]} {each[1]}: {each[3]}")

#actual output is commented here
# Here are my favorite romance movies:
# The Princess Bride 1987: The story of a man and a woman who lived happily ever after.
# Groundhog Day 1993: He's having the day of his life… over and over again.
# Amélie 2001: One person can change your life forever.
