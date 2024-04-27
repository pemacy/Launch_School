'''
Create a function that takes a list of integers as an argument and returns a
tuple of two numbers that are closest together in value. If there are multiple
pairs that are equally close, return the pair that occurs first in the list.
'''

def closest_numbers(lst):
    # Problem
    # takes a list of integers
    # returns tuple of two numbers that are closest in value
    # if multiple pairs occur, return the first that occurs

    # Data Structure
    # dictionary to store all closeness values and tuples that fall into them

    # Algorithm:
    # create empty list close_nums
    # loop through every element and find which is the closest
    # put both numbers in a tuple and append that to close_nums
    #
    pass
    storage = {}
    for _ in range(len(lst)):
        num = lst.pop(0)
        for n in lst:
            diff = abs(num - n)
            storage.setdefault(diff, [])
            storage[diff].append((num, n))
        lst.append(num)
    return storage[min(storage)][0]


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
