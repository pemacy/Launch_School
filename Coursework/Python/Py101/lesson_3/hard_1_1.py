'''
Will the following functions return the same results?
'''

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# no it won't, the second function will return None, the dict is unreachable code
