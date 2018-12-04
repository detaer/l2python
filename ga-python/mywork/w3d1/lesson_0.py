# 1. Declare a list with the names of your classmates
List_Of_Classmates = ["Galareh", "John", "Marco", "Josephine", "Chris"]
# 2. Print out the length of that list
print(len(List_Of_Classmates))
# 3. Print the 3rd name on the list
print(List_Of_Classmates[2])
# 4. Delete the first name on the list
removed = (List_Of_Classmates.pop(0))
# 5. Re-add the name you deleted to the end of the list
List_Of_Classmates.append(removed)

print(List_Of_Classmates)