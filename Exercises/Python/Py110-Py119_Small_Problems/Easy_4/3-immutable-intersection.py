'''
Transform two lists into frozensets and find their common elements.
'''

def find_intersection(l1, l2):
    return frozenset(set(l1) & set(l2))

print(find_intersection([2,4,6,8], [1,3,5,7,8]))
# frozenset({8})
