'''
pet.py
Name: Wengel Gemu
Collaborators: None
Date: October 4th, 2019
Description: Object to check dogs weight before and after feeding using inheritances
'''

class Dog(object):
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        # print(self.name)
        
    def eat(self, amount):
        self.weight += amount
        # print(self.name)
        # print(self.weight)

    def exercise(self, amount):
        self.weight -= amount
        
class Person(object):
    def __init__(self, name, dog, generosity):
        self.name = name
        self.dog = dog
        self.generosity = generosity
        
    def feedDog(self):
        ## YOUR CODE HERE
        # print("hi")
        # dog is fed based on persons generosity, adding values
        print(self.dog.weight + self.generosity)
        
# person and dog information
my_person = Person("Barack Obama", Dog("Bo", 30, "Portuguese Water Dog"), 0.9)

# check dogs weight
print("Bo's weight before feeding: ")
print(my_person.dog.weight)

# check dogs weight after person feeding
print("Bo's weight after feeding: ")
my_person.feedDog()



## YOUR CODE HERE

## Create a Person object.
##  -Choose any name (string) that you want.
##  -The dog parameter should be a Dog object that you create. (Choose any name (string), weight (float), and breed (string) that you want.)
##  -The generosity should be any floating point number such that 0 <= generosity <= 1

## Check the dog's weight. (How can you get the Dog object?)
## Have your Person object feed their pet dog.
## Check the dog's weight again.
