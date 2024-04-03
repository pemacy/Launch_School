'''
One day, Spot was playing with the Munster family's home computer, and he
wrote a small program to mess with their demographic data:
'''

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)

'''
Did the family's data get ransacked? Why or why not?
'''
# Yes, the value is a pointer to the dict object, it points to the same
# object as the munsters dict does, so by changing values in that dict
# you change the values everywhere

# to not do this you would have to do another loop through each dict like:
'''
for key1, value1 in value.items():
    if key == 'age':
        value1 += 42
    else:
        value1 = 'other'
'''
