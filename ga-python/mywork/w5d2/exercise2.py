#%%
#Generate a random number with random.randrange(). Print it out.
range_of_numbers = (94893983)
rando_number = random.randrange(range_of_numbers)
print(rando_number)

# Create a list, like deck = ["ten", "jack", "queen", "king", "ace"]
# Use random.choice() to pick a random card in your deck. Print it out.
deck = ["ten", "jack", "queen", "king", "ace", "tostada"]
pick_a_card = random.choice(deck)
print(pick_a_card)

# Use random.shuffle() to mix up your deck; print that out.
random.shuffle(deck)
print(deck)