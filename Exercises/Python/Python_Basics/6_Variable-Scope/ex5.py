'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

a = 1

def my_function():
    print(a)
    a = 2

my_function()

'''
I think it will give an error because it tries to define 'a' in the block
I'm assuming Python does a first pass before it executes and determine knows 'a' will be defined in the block, so any prior usage of 'a' will be undefined
If it doesn't do a first pass then it will print 1
'''

# runs code

'''
I was correct, it throws an UnboundError
Python detects that a is being assigned within the my_function function and
therefore treats it as a local variable. However, since we are trying to print
the local a variable's value before it has been assigned a value, we get an error.
'''
