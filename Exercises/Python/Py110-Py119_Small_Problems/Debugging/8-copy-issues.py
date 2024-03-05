'''
We have a list of lists and want to make a copy of it. After making the copy, we modify the original list, but the copied list also seems to be affected:
'''

'''
It's not a deep enough copy, use copy.deepcopy(original)
'''

import copy

original = [[1], [2], [3]]
# Original Code:
# copied = copy.copy(original)

# Updated Code:
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0])  # Expected: [1]
