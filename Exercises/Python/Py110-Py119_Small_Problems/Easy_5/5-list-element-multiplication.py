'''
Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.
'''

def multiply_elements(l1, l2):
    return [ n1 * n2 for n1, n2 in zip(l1, l2) ]

print(multiply_elements([1, 2, 3], [4, 5, 6]))
# [4, 10, 18]
