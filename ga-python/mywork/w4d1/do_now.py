class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(self.name)
        # print(self.age)
        # print(self.species)
    
    def display_details(self):
        print(self.name)
        print(self.age)
        print(self.species)

#Instructions: Instantiate two instances of the Dog class below, one as a variable called fido and the other as a variable called fluffy. 
# fido should have the name "Fido" and be 5 years old; fluffy should have the name "Fluffy" and be 1 years old
fluffy = Dog("Fluffy", 1)
fluffy.display_details()

fido = Dog("Fido", 5)
fido.display_details()


print("shitsnacks")