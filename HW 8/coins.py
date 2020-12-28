'''
coins.py
Name: Wengel Gemu
Date: November 3, 2019
Desscription: memoize a recursive solution for minimum number of coins
'''

import math 

memo = {}
def memoized_change(number, coins):

    if number in memo:
        if coins in memo:
            return memo[number, coins]

    if number <= 0:
        return 0

    elif coins == []:
        result = math.inf
        return result

    loseIt = memoized_change(number, coins[1:])
    if number < coins[0]:
        result = loseIt
        return result
    else:
        useIt = 1 + memoized_change(number - coins[0], coins)
        result = min(useIt, loseIt)
        return result
    
    memo[number, coins] = result
    return result

print(memoized_change(48, [1, 5, 10, 25, 50, 100]))
print(memoized_change(48, [ 5, 10, 25, 50, 100]))


def change(number, coins):
    if number <= 0:
        return 0
    elif coins == []:
        return math.inf

    loseIt = change(number, coins[1:])
    if number < coins[0]:
        return loseIt
    else:
        useIt = 1 + change(number - coins[0], coins)
        return min(useIt, loseIt)

print(change(48, [1, 5, 10, 25, 50, 100]))
print(change(48, [ 5, 10, 25, 50, 100]))
