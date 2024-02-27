dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

"""
the dict() constructor creates a shallow copy of a dictionary
therefore any lists referenced by a key of dict1 will also be referenced by dict2
any changes to the lists will be seem by the other dict referencing that list
so the result will print [1, 42, 3]
"""
