'''
We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?
'''

'''
remove() is not a method on the 'set' datatype
need to converto to a list first, remove the items, then convert back to a set
OR
you can remove using the set difference method or operation: {set} 
'''

data_set = {1, 2, 3, 4, 5}

'''
Old Code
for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)
'''

'''
New Code
'''

for item in data_set:
    if item % 2 == 0:
        data_set = data_set - {item}

print(data_set)
