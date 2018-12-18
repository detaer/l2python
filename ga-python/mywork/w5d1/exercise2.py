#%%

my_file = open("a_file.txt", "r")
file_contents = my_file.read()
my_file.close


my_file2 = open("c_file.txt", "w")
my_file2.write(file_contents)
my_file2.close()