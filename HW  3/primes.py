'''
primes.py
Name: Wengel Gemu
Collaborators:
Date: September 20, 2019
Description: This program returns the first N primes.
'''


def is_prime(num):
    # TODO: add your code here for checking whether num is prime
    if num == 1:
        print(str(num) + " is not a prime number")
        return False
    if num == 2:
        print(str(num) + " is a prime number")
        return True

    if num > 0:
        # checking prime status of number
        for value in range(2, num):
            if ((num % 3) == 0):
                print(str(num) + " is not a prime number")
                return False
            elif ((num % value) == 0):
                print(str(num) + " is not a prime number")
                return False
            else:
                print(str(num) + " is a prime number")
                return True

    # providing output for when num is negative
    else:
        print(str(num) + " is not a positive integer")
        return False
   


def primes(N):
    # TODO: add your code here for finding the first N primes
    count = 0
    primes_list = []
    while len(primes_list) < N:
        if is_prime(count):
            primes_list.append(count)
        count += 1
        print(primes_list)
    return primes_list


# TODO: ensure that your functions pass the following tests
# think about what you expect the program to print out if your code works
print("#1")
print(not is_prime(1))
print(" ")

print("#2")
print(is_prime(2))
print(" ")

print("#3")
print(is_prime(3))
print(" ")

print("#4")
print(not is_prime(4))
print(" ")

print("#5")
print(is_prime(5))
print(" ")

print("#6")
print(not is_prime(9))
print(" ")

print("#7")
print(primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
print(" ")

print("#8")
print(is_prime(-1))
print(" ")
