'''
member.py
Name: Wengel Gemu
Date: October 11, 2019
Description: Writing a recursive function that returns true if item is in my_list
'''

def member(item, my_list, count = 0):
    # handles case if list is empty
    if len(my_list) == 0: 
        print('list is empty')
        return False
    # returns true if item is in the list
    elif item == my_list[count]:
        print('item in list') 
        return True
    else:
        # looks through list
        if count < 6:
            return member(item, my_list, count+1)
        else:
            # returns false if item is not in the list
            print('item not in list')
            return False

print(member(7, [1, 2, 3, 4, 6, 7, 9]))
