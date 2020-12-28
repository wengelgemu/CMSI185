'''
hotandcold.py
Name: Wengel Gemu
Collaborators:
Date: September 20, 2019
Description:
'''

# This program uses MIT card counting information to tell 
# the user when the current deck is hot (it's time to bet 
# big!) or cold (leave the table). It gets user input and
# then keeps track of the MIT card counting score so far.
# It should loop and keep asking you for cards until the
# table becomes hot or cold.

# Write some code that keeps track of the current count for 
# the cards that the user inputs.
# Your count should start at 0 and either go up 1, down 1, 
# or remain the same every time the user inputs a card 
# depending on the value of that card as stated in cardcountvalue.py.

# this is a list containing all of the valid values for a card
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

# store the count as a variable named count.
# TODO: Fill in the value it starts at here.
count = 0

# Your code should loop and print the new count after every
# time the user inputs a new card.

# TODO: start a loop here, and ask for user input (use code from ps1)



for card_value in cards:
        card_value = input("Enter a card value: ")
        if card_value in ['2','3','4','5','6']:
            count += 1
            # print("the count is " + str(count))
        elif card_value in ['7','8','9']:
            count += 0
            # print("the count is " + str(count))
        elif card_value in ['10','J','Q','K', 'A']:
            count -= 1
            # print("the count is " + str(count))
        else:
            # response for if the count not one of the card values
            print("the count is invalid")
            # tell the user their number is growing! hot hot!!
        if count >= 5:
            print("hot! bet BIG!!")
            # tell the user their number is shrinking! cold cold!!
        elif count <= -5:
            print("cold! maybe you should find a new table...")



# TODO: in the loop, add the card counting value to the running total count
# use code from ps1 to get the card counting value

# TODO: in the loop, add some statements that check if the count
# is >= 5 (hot) or <= -5 (cold). If the count ever gets hot
# or cold, print a message saying the deck is hot/cold and
# exit the loop.

# NOTE: card counting isn't illegal but it IS effective, so 
# the casinos don't like to let their players do it! Make 
# sure to keep your current count secret (don't print it)
# and only print a message when the deck gets hot or cold. 
