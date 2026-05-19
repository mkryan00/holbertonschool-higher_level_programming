#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 100):
        if num % 5 == 0 and num % 3 == 0:
            print(f'FizzBuzz', end=" ")
        if num % 5 == 0:
            print(f'Buzz', end=" ")
        if num % 3 == 0:
            print(f'Fizz', end =" ")
        else:
            print('{:d}'.format(num), end=" ")
            
