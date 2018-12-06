# John Lewis w3d1 homework
# My favorite romance movies
# title, release year, runtime, tagline, main characters
romantic_movie1 = ("The Princess Bride", 1987, 98, "The story of a man and a woman who lived happily ever after.", ["Buttercup", "Westley", "Fezzik", "Inigo Montoya", "Vizzini"])
romantic_movie2 = ("Groundhog Day", 1993, 101, "He's having the day of his life... over and over again.", ["Phil Connors"])
romantic_movie3 = ("Amélie", 2001, 122, "One person can change your life forever.", ["Amélie Poulain", "Nino Quincampoix", "The Garden Gnome"])
romantic_movies = (romantic_movie1, romantic_movie2, romantic_movie3)
# expected output
# Here are my favorite romance movies:
# The Princess Bride (1987): The story of a man and a woman who lived happily ever after.
# Groundhog Day (1993): He's having the day of his life...over and over again.
# Amélie (2001): One person can change your life forever.

print("Here are my favorite romance movies:")

for each in romantic_movies:
    print(f"{each[0]} ({each[1]}): {each[3]}")

#actual output is commented here
# Here are my favorite romance movies:
# The Princess Bride (1987): The story of a man and a woman who lived happily ever after.
# Groundhog Day (1993): He's having the day of his life... over and over again.
# Amélie (2001): One person can change your life forever.

=============================================

# John Lewis w3d1 homework2
employees = [{
    "name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": "$87,000"
},
{
    "name": "Leslie Knope",
    "age": 43,
    "department": "Middle Management",
    "phone": "555-4321",
    "salary": "$97,000"
},
{
    "name": "Andy Dwyer",
    "age": 29,
    "department": "Management",
    "phone": "555-1122",
    "salary": "$22,000"
},
{
    "name": "April Ludgate",
    "age": 21,
    "department": "Administration",
    "phone": "555-3345",
    "salary": "$187,000"
}
]
# employees = ["Bitter_Moustache_Employee", "Waffle_Boss_Employee", "Dave_Matthews_Tribute_Employee", "Modest_Goth_Employee"]
# employees = [Bitter_Moustache_Employee, Waffle_Boss_Employee, Dave_Matthews_Tribute_Employee, Modest_Goth_Employee]
# expected output
# Ron Swanson in Management can be reached at 555-1234.
# Leslie Knope in Middle Management can be reached at 555-4321.
# Andy Dwyer in Shoe Shining can be reached at 555-1122.
# April Ludgate in Administration can be reached at 555-3345.
for each in employees: 
    print(each["name"], " in ", each["department"], " can be reached at ", each["phone"], ".", sep='')

# actual output
# Ron Swanson in Management can be reached at 555-1234.
# Leslie Knope in Middle Management can be reached at 555-4321.
# Andy Dwyer in Management can be reached at 555-1122.
# April Ludgate in Administration can be reached at 555-3345.
