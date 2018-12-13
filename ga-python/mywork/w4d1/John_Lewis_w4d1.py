#%%
class Football_Team():

    def __init__(self):
        self.offense = False
        self.defense = False
        self.rule_changes = False

    def get_offense(self):
        self.offense = True
        return self.offense

    def get_defense(self):
        self.defense = True
        return self.defense

    def get_rule_changes(self):
        self.rule_changes = True
        return self.rule_changes

jaguars = Football_Team()

offense = jaguars.get_offense()
defense = jaguars.get_defense()

if jaguars.offense and jaguars.defense:
    rule_changes = jaguars.get_rule_changes()

print("How are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
    print("We're going to the Super Bowl!")
else:
    print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")


#%%
print("1. Coercion is another term for which of the following concepts in Python?\n","d) Implicit type conversion", sep='')
print("")
print("2. Type casting is another term for which of the following concepts in Python?\n","c) Explicit type conversion", sep='')
print("")
print("3. What function in Python can we use to check a variable's type?\n","a) type()", sep='')
print("")
print("4. Which of the following is NOT a primitive data structure?\n","c) List", sep='')
print("")
print("5. According to the article, what is the main reason to convert a tuple into a list?\n","Tuples are immutable data type and allows substantial optimization to the programs that you create.", sep='')
