'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)


'''
it will print 2, the global keyword binds the variable 'a' to the global variable 'a'
'''
