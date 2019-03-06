age = int(input("Gimme your age: "))


if age < 12:
    print('You are not Alice, kiddo.')
elif age >= 12 and age <= 99:
    print("You aren't dead yet, quit freaking out.")
elif age >= 100 and age <= 1999:
    print('you are between 100 and 2000 years old but not including 2000.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
