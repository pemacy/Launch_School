'''
Create a function that takes an list of integers as an argument and returns
the integer that appears an odd number of times. There will always be exactly
one such integer in the input list.
'''

def odd_fellow(lst):
    # Problem
    #   Input - list of integers
    #   Output - integer in the list that appears an odd number of times

    # Data Structure
    #   Set of numbers in list to loop through
    #   Dictionary of key = number, value = count

    # Algorithm
    #   loop through set of numbers
    #       count the number of times it appears in the lst
    #       add this to the dictionary
    #   comprehension to filter all number without an odd count
    #   return the number in filtered list

    lst_set = set(lst)
    d = {}
    for n in lst_set:
        d[n] = lst.count(n)

    odd_counts = [ n for n, c in d.items() if c % 2 != 0 ]
    return odd_counts[0]

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)
