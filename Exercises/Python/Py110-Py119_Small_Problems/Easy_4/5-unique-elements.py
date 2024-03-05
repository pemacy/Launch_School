'''
From two lists, determine the elements that are unique to the first list.
'''

def unique_from_first(l1, l2):
    return set(l1) - set(l2)

print(unique_from_first([3,6,9,12], [6,12,15,18]))
# {9, 3}
