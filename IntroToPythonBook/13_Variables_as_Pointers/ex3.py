dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

"""
dict() is a constructor method and creates a new object
because of this:
    dict2 is not dict1
    but: dict2 == dict1

if you mutate dict2, it will not affect dict1, do dict1['Monty Python'] will = 'Life of Brian' still
"""
