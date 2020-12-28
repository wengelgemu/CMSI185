'''
translator.py
Name: Wengel Gemu
Collaborators:
Date: September 28th, 2019
Description: Translates from English numbers to Spanish (or your language of choice!).
'''

## Here are the Spanish numbers, spelled out from 0 to 9:
## cero uno dos tres cuatro cinco seis siete ocho nueve

# dictionary holding english and spanish numbers
eng2sp = {"zero" : "cero", "one" : "uno", "two" : "dos", "three" : "tres", "four" : "cuatro", "five" : "cinco", "six" : "seis", "seven" : "siete", "eight" : "ocho", "nine" : "nueve"}

## Ask the user to input multiple single-digit English numbers, separated by spaces
eng_num = input("Enter one (or more) numbers spelled out in English: ")
eng_list = eng_num.split(" ")

# print(eng_list)
list = []
for word in eng_list:
    spnum = eng2sp[word]
    # add new value to list of translated numbers
    list.append(spnum)
    # print("The Spanish translation is: " +  eng2sp[word])

## Print out the Spanish translation of each English number (in order)
print("The Spanish translation is: " +  (' '.join(list)))
