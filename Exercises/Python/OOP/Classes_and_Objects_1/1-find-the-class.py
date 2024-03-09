'''
Update the following code so that, instead of printing the values, each statement prints the name of the class to which it belongs.
'''

# Comments show expected output
print("Hello")                # <class 'str'>
print(5)                      # <class 'int'>
print([1, 2, 3])              # <class 'list'>

print("Hello".__class__)
x = 5
print(x.__class__)
print([1,2,3].__class__)
