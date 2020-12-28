'''
cardcountvalue.py
Name: Wengel Gemu
Collaborators: None 
Date: September 6th, 2019
Description: This program takes user input of a card value and prints
the card counting number for that card.
'''


# MIT card counting values:
#
#    2 - 6 should add one to the count, so their value is 1
#    7 - 9 have no effect on the count, so their value is 0
#    A, 10, J, Q, and K should subtract one from the count,
# so their value is -1



# this is a list containing all of the valid values for a card
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

card_value = input("Enter a card value: ")
count = 0


if card_value in ['2','3','4','5','6']:
    count += 1
    print("the card is " + str(count))
elif card_value in ['7','8','9']:
    count += 0
    print("the card is " + str(count))
elif card_value in ['10','J','Q','K', 'A']:
    count -= 1
    print("the card is " + str(count))
else:
    print("the card is invalid")

# Write some code that takes a card as input (remember to 
# check it for validity) and outputs the MIT card counting 
# value of that card. Use multiple if/else statements
# to determine the card counting value of the user's input.
