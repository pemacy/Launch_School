'''
Given a dictionary and a list of keys, produce a new dictionary that only retains the entries with the specified keys.
'''

def keep_keys(hsh, lst):
    new_hsh = {}
    for key in hsh:
        if key in lst:
            new_hsh[key] = hsh[key]
        else:
            continue
    return new_hsh

print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['red', 'blue']))
# {'red': 1, 'blue': 3}
