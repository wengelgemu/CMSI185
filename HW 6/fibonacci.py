'''
fibonacci.py
Name: Wengel Gemu
Date: October 9, 2019
Description: Compare iterative and recursive fibonacci.
'''

import time

def fib_recur(n):
    """recursive fibonacci"""
    # YOUR CODE HERE
    # solve recursively by calling function
    if n >= 2:
        val = fib_recur(n-1) + fib_recur(n-2)
        return val
    else:
        return n


def fib_iter(n):
    """iterative fibonacci"""
    # YOUR CODE HERE
    # solve iteratively with for loop
    fn0 = 0
    fn1 = 1
    for i in range(0, n):
        val = fn0
        fn0 = fn1
        fn1 = val + fn1
    return fn0


# test values and speed of recursive
start_recur = time.time()
print(fib_recur(5))
end_recur = time.time()
print('Recursive Fibonacci took', (end_recur - start_recur) * 1000, 'ms')

# test values and speed of iterative
start_iter = time.time()
print(fib_iter(5))
end_iter = time.time()
print('Iterative Fibonacci took', (end_iter - start_iter) * 1000, 'ms')
