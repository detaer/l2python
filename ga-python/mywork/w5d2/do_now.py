#%%
# 1
old_list = ['convert', 'this', 'to', 'a', 'list', 'comprehension']

#### convert these three lines to a one-line list comprehension.
new_list = []
for word in old_list:
    new_list.append(word + ' POW')
####
newest_list = [word + ' pow' for word in old_list]

print(new_list)
print(newest_list)

#%%
# 2
old_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]

#### convert these four lines to a one-line list comprehension.
new_list = []
for num in old_list:
    if num % 2 == 0:
        new_list.append(num)
####

newest_list = [num for num in old_list if num % 2 == 0]

print(new_list)
print(newest_list)

%##

# BONUS
old_list = [1,2,3,4,5]

#### convert these four lines to a one-line list comprehension.
new_list = []
for item1 in old_list:
    for item2 in old_list:
        new_list.append(item1 * item2)
####

print(new_list)
