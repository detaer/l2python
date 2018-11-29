# def reassurance():
#     print("Good job, Chris!")
#     print("You are strong")
#     print("You are capable")
#     print("You are worthy of love")

# reassurance()
# disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]

# def impliment_IOU():
#     for name in disney_characters:
#         if "u" in name:
#             print(name, "U are so Uniquely U!")
#         elif "i" in name:
#             print(name, "I bet you're Impressively Intelligent!")
#         elif "o" in name:
#             print(name, "O My - How Original!")
#         else:
#             print(name, "Ehh, a's and e's are so ordinary.!")

# impliment_IOU()

# def print_IOU(list_of_names):
#     for name in list_of_names:
#         if "u" in name:
#             print(name, "U are so Uniquely U!")
#         elif "i" in name:
#             print(name, "I bet you're Impressively Intelligent!")
#         elif "o" in name:
#             print(name, "O My - How Original!")
#         else:
#             print(name, "Ehh, a's and e's are so ordinary.!")
# print_IOU(list_of_names = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"])

# def item_and_tax(price):
#         tax_rate = .08
#         total_amount = price + (price * tax_rate)
#         print("The total, with tax is $", total_amount)
# 
# item_and_tax(8.75)

# candidate_number = 1

# def fizzbuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# 
# while candidate_number <= 100:
#     fizzbuzz(number = candidate_number)
#     candidate_number += 1

# def mystery():
#    return 6
#    return 5
#
# my_number = mystery()
# print(my_number)

# def add_bonus_points(score):
#     if score > 50:
#         return score + 10
#     score += 20
#     return score

# total_points = add_bonus_points(55)
# print(total_points)

# def rock_and_roll(muted):
#     song = "It's only Rock 'N' Roll"
#     artist = "Rolling Stones"

#     if (muted == True):
#         return
#         # Here, we use return as a way to exit a function
#         # We don't actually return any value.
#     print("Now playing: ", song, " by ", artist)

# rock_and_roll(False)

# def categorize(x):
#   if (x < 8):
#       return 8
#   x += 3
#   if (x < 15):
#       return x
#   return 100

# number = categorize(x = 13)
# print(number)

