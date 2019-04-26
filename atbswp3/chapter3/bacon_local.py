def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
print(eggs)
spam()
next_Method()

print(eggs)