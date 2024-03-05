'''
Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.
'''

def unique_sequence(lst):
    new_lst = []

    for i, el in enumerate(lst):
        if i == 0 or lst[i-1] != el:
            new_lst.append(el)
        else:
            continue
    return new_lst

print(unique_sequence([1, 1, 2, 3, 3, 3, 4, 5, 5, 6]))
# [1, 2, 3, 4, 5, 6]
