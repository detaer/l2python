list_of_nums = [1,2,3,5,6,12,21,18,14,20,19]
even_nums = []
for num in list_of_nums:
    if num % 2 == 0:
        even_nums.append(num)

print(even_nums)