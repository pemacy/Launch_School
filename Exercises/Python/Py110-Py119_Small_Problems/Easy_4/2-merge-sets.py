'''
Given two lists, convert them to sets and return a new set which is the union of both sets.
'''

def merge_sets(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1 | s2

print(merge_sets([3,5,7,9], [5,7,11,13]))
# {3, 5, 7, 9, 11, 13}
