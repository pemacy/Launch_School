'''
Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.
'''

def sum_of_sums(lst):
    return [ sum(lst[:i+1]) for i, el in list(enumerate(lst)) ]

print(sum_of_sums([3, 5, 2]))        # (3) + (3 + 5) + (3 + 5 + 2) --> 21
print(sum_of_sums([1, 5, 7, 3]))     # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
print(sum_of_sums([4]))              # 4
print(sum_of_sums([1, 2, 3, 4, 5]))  # 35
