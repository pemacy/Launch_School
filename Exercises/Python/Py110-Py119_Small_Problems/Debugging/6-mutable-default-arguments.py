'''
We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly:
'''

'''
Default parameter values are evaluated from left to right when the function definition is executed. This means that the expression is evaluated once, when the function is defined, and that the same “pre-computed” value is used for each call. This is especially important to understand when a default parameter value is a mutable object, such as a list or a dictionary: if the function modifies the object (e.g. by appending an item to a list), the default parameter value is in effect modified. This is generally not what was intended. A way around this is to use None as the default, and explicitly test for it in the body of the function
'''

'''
Old
'''
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

'''
New
'''
def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1))        # Expected: [1]
print(append_to_list(2))        # Expected: [2]
print(append_to_list(3))        # Expected: [3]
