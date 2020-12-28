'''
exponential.py
Name: Wengel Gemu
Date: October 9, 2019
Description: Writing a recursive function to calculate exponents
'''

def exponential(base, exp):
    # if exp is zero the value is zero
    if exp == 0:
        return 0
    # if exp is one the value is itself
    elif exp == 1:
        return base
    # perform exponent
    else:
        base = base * exponential(base, exp - 1)
    return base

print(exponential(10, 2))
