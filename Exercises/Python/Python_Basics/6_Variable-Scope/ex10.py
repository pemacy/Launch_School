'''
What will the following code do and why? Don't run it until you have tried to answer.
'''

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)


'''
it will print [10, 2, 3] - 'b' in the function block references the block above it because lists are mutable and can be changed
therefore it is not a re-assignment of a variable, it is a mutation of a variable
'''
