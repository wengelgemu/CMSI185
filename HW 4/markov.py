'''
markov.py
Name: Wengel Gemu
Collaborators: Kira Toal, Shane Delaney
Date: September 29, 2019
Description: Performs Markov analysis on novel in textfile  
'''
import random

text_file = open('sherlock.txt', 'r')
# split a line of text into a list of words
lines = text_file.read().split() 
print("the number of lines is: " + str(len(lines)))

# text_file.close()

dictionary = {}
i = 0
while i <= 150:
    if lines[i] in dictionary.keys():
        # make book file into a list
        dictionary[lines[i]].append(lines[i + 1])
        # print(dictionary[lines[1]])
    else:
        dictionary.update({lines[i]: ''})
        dictionary[lines[i]] = lines[i + 1].split()
        # print(dictionary[lines[1]])
    # iterates while loop
    i += 1


x = 0 
wordlist = []
prefix = random.choice(list(dictionary))
wordlist.append(prefix)
while x <= 25:
    s = random.choice(dictionary[prefix])
    wordlist.append(s)
    prefix = s

    # turns list into a sentence, adds spaces
    # makes text lowercase instead of random upper and lower
    sentence = ' '.join(wordlist).lower()

    # iterates while loop
    x += 1
print(sentence)
