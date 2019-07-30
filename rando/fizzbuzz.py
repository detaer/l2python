#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

candidate_number = 1



def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

while candidate_number <= 100:
    fizzbuzz(number = candidate_number)
    candidate_number += 1

