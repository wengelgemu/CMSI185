'''
cardlist.py
Name: Wengel Gemu  
Collaborators: None 
Date: September 6th, 2019
Description: This program checks user input against a list to see if it is valid.
'''


# this is a list containing all of the valid values for a card
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

card_value = input("Enter a card value: ")

if card_value in cards:
    print("the card is valid")
else:
    print("the card is invalid")

# Write some code that prompts the user to enter a 
# card value and then checks if it is valid or 
# not. Print a message saying whether
# or not the card is valid.

# (hint: think about what operator you would use
# to see if a value is in a list)
