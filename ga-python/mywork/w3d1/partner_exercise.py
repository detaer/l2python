# You know the drill: Grab a partner and pick a driver!

# Write a script that declares a dictionary called my_name.
# my_name = {}

# Add a key for each letter in your name with a value of how many times that letter 
# appears.
# As an example, here is the dictionary you'd make for "Callee":
# my_name = 
my_name = {"c": 1, "a": 1, "l": 2, "e": 2}
my_name['j'] = 1
print(my_name)
# Make a for-loop that goes through each letter in your dictionary and prints 
# out the key and value.
for letter in my_name:
    print(letter, ":", my_name[letter])
# Bonus (if you have time): Change the print statement so that instead of 
# printing just the key and value, it prints a sentence like The letter l 
# appears in my name once or The letter l appears in my name twice.