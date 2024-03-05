'''
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.
'''

def invert_dict(hsh):
    return { hsh[key]: key for key in hsh }

print(invert_dict({'apple': 'fruit', 'broccoli': 'vegetable', 'salmon': 'fish'}))
# {'fruit': 'apple', 'vegetable': 'broccoli', 'fish': 'salmon'}
