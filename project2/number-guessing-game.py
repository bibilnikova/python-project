"""
The program selects a random number between two numbers,
the user guesses the correct number.
"""

import random
a = int(input('Enter the first number: '))
b = int(input('Enter the last number: '))
n = random.randint(a, b)
guess = int(input('Enter any number: '))
while n != guess:
    if guess < n:
        print('Too low')
        guess = int(input('Enter number again: '))
    elif guess > n:
        print('Too high')
        guess = int(input('Enter number again: '))
    else:
        break
print('You guessed it right!')
