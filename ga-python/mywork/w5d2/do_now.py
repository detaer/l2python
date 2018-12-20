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