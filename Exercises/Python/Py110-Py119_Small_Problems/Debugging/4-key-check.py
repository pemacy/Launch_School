'''
You have a function that should check if a key exists in a dictionary and return its value. However, it's raising an error. Why is that?
'''

'''
Because it is not using the dict.get() function.
Referencing a key in a dictionary that does not exist raises an error unless you use the 'get' method
'''

'''
Old
'''
def get_key_value(d, key):
    if d[key]:
        return d[key]
    else:
        return None

'''
New
'''
def get_key_value(d, key):
    if d.get(key):
        return d[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))
