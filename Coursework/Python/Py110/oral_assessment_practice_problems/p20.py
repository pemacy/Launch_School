'''
Create a function that takes a list of numbers, all of which are the same
except one. Find and return the number in the list that differs from all the
rest.

The list will always contain at least 3 numbers, and there will always be
exactly one number that is different.
'''

def what_is_different(lst):
    # Problem:
    #   Input - list of numbers
    #   Output - integer in the list that differs from the rest
    #   Rules
    #       find the number that has a count of 1
    #       number will be integer or float
    #       lst will always have at least 3 numbers
    #   Assumptions:
    #       list will have only numbers and at least 3 elements
    #   Edge Cases:
    #       empty list
    #       invalid elements

    # Data Structure
    #   Set of list

    # Algorithm
    #   loop through set of list and count amount of times they occur in the list
    #   return the number that only has count of 1

    return [ el for el in set(lst) if lst.count(el) == 1 ][0]



print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
