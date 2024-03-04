'''
Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.
'''

def union(l1, l2):
    for el in l2:
        if el not in l1:
            l1.append(el)
        else:
            pass
    return set(l1)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
