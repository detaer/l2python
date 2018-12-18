#%%
# DO NOW: use a for-loop to print the name of each Male in this nested dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}

for p in people:
    if people[p]['sex'] == 'Male':
        print(people[p]['name'])