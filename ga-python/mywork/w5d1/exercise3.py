#%%
user_name = input("Please type your name:")
favorite_food = input("What do you eat?")

print(user_name)
print(favorite_food)

my_file = open('newfile.txt', 'w')
my_file.write("my name is" + user_name + "my favorite food is" + favorite_food)
my_file.close()