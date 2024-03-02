'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

a = 1

def my_function():
    a = 2

my_function()
print(a)

'''
it will print 1, the function creates a local variable 'a' that does not affect the scope above it
'''
