'''
Consider these two simple functions:
'''

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

'''
What will this return?
'''

print(bar(foo()))

# it will return "no"
