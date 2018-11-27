angry = True
bored = True
hungry = False
tired = False

# Example `if` statement:
# if bored:
#    print("T-Rex roars! Rawr!")

# If T-Rex is angry, hungry, and bored he will eat the Triceratops.
if angry and hungry and bored:
    print("Eat the Triceratops")
# Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
elif tired and hungry:
    print("Eat the Iguanadon")
# Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
elif hungry and bored:
    print("Eat the Stegasaurus")
# Otherwise if T-Rex is tired, he goes to sleep.
elif tired:
    print("Is le tired.")
# Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
elif angry and bored:
    print("fight with the Velociraptor")
# Otherwise if T-Rex is angry or bored, he roars.
elif angry or bored:
    print("he roars.")
# Otherwise T-Rex gives a toothy smile.
else:
    print("T-Rex gives a toothy smile.")