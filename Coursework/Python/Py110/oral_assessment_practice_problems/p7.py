'''
Create a function that takes a list of integers as an argument and returns the
number of identical pairs of integers in that list. For instance, the number
of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For
instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2.
The first list contains two complete pairs while the second has an extra 2
that isn't part of the other two pairs.
'''

def pairs(lst):
    # Problem
    # takes list of integers
    # returns number of identical pairs
    # empty list or only one value return 0
    # count each complete pair once
    #   if a number occurs 4 times, that's 2 pairs
    #   if three of one number that makes only 1 pair

    # Data Structure: none

    # Algorithm
    #   pair_count = 0
    #   for element in set(list)
    #       pair_count += list.count(el) // 2
    #   return pair_count

    pair_count = 0
    for n in set(lst):
        pair_count += lst.count(n) // 2

    print(pair_count)
    return pair_count

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
