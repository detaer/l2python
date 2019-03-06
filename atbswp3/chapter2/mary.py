name = input("What is your name:")
password = input("What is your pasword:")

if name == 'Mary':
    print('Hello Mary, why do you trust me with your name and password? Do you tell that to all the robots?')
    if password == 'swordfish':
        print('You have lots of trust by giving me your password')
    else:
        print(f"You are wise not to trust me {name}." )
else:
    print('I WAS EXPECTING MARY, GET OUT!')