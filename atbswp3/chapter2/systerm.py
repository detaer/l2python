import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit(0)
    print('You typed ' + response + '.')