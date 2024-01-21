# create a number guessing game
# generate a  random number within range of 1 - 10
# the user will have the option to guess the secret number
# the program will provide the user feedback based on their input
# i.e, if guess is too big, small, or equal to their secret number
# if user guessed the secret number then program terminates

import random
secret_number = random.randint(1, 100) #generates random number within the range of 1 - 100
while True:
    user_guess = int(input('Guess the secret number between 1 - 100 '))
    if user_guess == secret_number:
        print('You guessed correctly!')
        print(secret_number)
        break
    elif user_guess > secret_number:
        print('Ooops! Your guess is higher than the secret number')
    elif user_guess < secret_number:
        print('Yikes! Your guess is lower than the secret number')