#%%
# Find all of the numbers from 1-1000 that are divisible by 7

number_divis_by_7 = [i for i in range(1, 1001) if i % 7 == 0 ]

print(number_divis_by_7)

#%%
# Create a list of all square numbers formed by squaring the numbers from 1 to 1000.

squares_to_the_moon = [i ** 2 for i in range(1,1001)]
print(squares_to_the_moon)

#%%
stringy = 'Where do you go to get tacos and pants?'
vowels = ['a', 'e', 'i', 'o','u','y']
strng = [letter for letter in stringy if letter.lower() not in vowels]

print(strng)

#%%
words_words_words = 'Where do you go to get tacos and pants?'
space_count = 0
count_dem_spaces = [character for character in words_words_words if character == ' ']
print(len(count_dem_spaces))

#%%
# List all the names in this list which have the letter 'i' in it (I added this one): 
names = ['Adam', 'Adnan', 'Alicia', 'Andrew', 'Charlie', 'David', 'Dominic', 'Etienne', 'John']
names_with_i = [name for name in names if 'i' in name]
print(names_with_i)

#%%
# Find all of the words in a string that are less than 4 letters
silly_string = "What is so funny about string? I don't see anything funny about this string"
short_words_for_trump = {word for word in silly_string.split() if len(word) < 4 }

print(short_words_for_trump)