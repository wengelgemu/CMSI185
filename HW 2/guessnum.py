'''
not_equal.py
Name: Wengel Gemu
Collaborators: 
Date: September 14, 2019
Desscription: This program implements the Guess My Number! game.
'''

import random

# def guess_compare(x):
#     print("Ready to guess? My number is between 0 and 30.")
#     print("Enter your guess now: ")
#     print ("? ")

#     # set up input for user and limits on random number assignment
#     a = input()
#     b = random.randint(0, 30)
    
#     # gives user response/hint for the game
#     if x <= 0:
#         print("out of tries! the answer is " + str(b))
#     elif str(a) == str(b):
#         print("Correct! You win!")
#         return
#     elif str(a) > str(b):
#         print("Too high!")
#     elif str(a) < str(b):
#         print("Too low!")
#     guess_compare(x-1)
# guess_compare(5)
# print(guess_compare())

def guess_compare(x):
    print("Ready to guess? My number is between 0 and 30.")
    print("Enter your guess now: ")
    print ("? ")

    # set up input for user and limits on random number assignment
    a = input()
    b = random.randint(0, 30)
    
    # gives user response/hint for the game
    if x <= 0:
        print("out of tries! the answer is " + str(b))
    elif int(a) == int(b):
        print("Correct! You win!")
        return
    elif int(a) > int(b):
        print("Too high!")
    elif int(a) < int(b):
        print("Too low!")
    guess_compare(x-1)
guess_compare(5)
print(guess_compare())



# Have your program generate a random number for the user
# to guess. Write a function that asks the user for a guess and 
# prints out whether it was too high, too low, or correct.
# Give the user five guesses. If the user hasn't guessed by
# then, print out the correct number.
