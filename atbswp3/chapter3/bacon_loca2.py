def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = '42'
ham()
spam()
ham()
bacon()
ham()