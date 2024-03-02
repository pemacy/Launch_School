'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

'''
it will print an error:
    UnboundLocalError: cannot access local variable 'x' where it
    is not associated with a value
because we are assigning something to 'x', any other references to 'x' will not include the global scope, so if 'x' is undefined in the function and used in assignment of itsel, it will raise an error
'''
