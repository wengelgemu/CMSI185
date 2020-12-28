'''
insertion_sort.py
Name: Wengel Gemu
Date: November 3, 2019
Desscription: Recursive insertion sort.
'''

def insert(x, sorted_list):
    """
    Returns the final sorted list containing x in the correct position.
    """
    # base cases
    if sorted_list == []:
        ### TODO: your code here! ###
        return [x]
    elif x < sorted_list[0]:
        ### TODO: your code here! ###
        return [x] + sorted_list

    # recursive case
    else:
        ### TODO: your code here! ###
        return sorted_list[0:1] + insert(x, sorted_list[1:])

def sort(my_list):
    # base case
    if my_list == []:
        return my_list
    else:
    # recursive case
        return insert(my_list[0], sort(my_list[1:]))

print(sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
