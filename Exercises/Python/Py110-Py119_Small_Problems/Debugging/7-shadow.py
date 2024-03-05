'''
We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?
'''

'''
The code is using a name for the function that is already used by the built in function sum(), and wanting to use the built-in function functionality even though they overwrote it in the function definition
'''

'''
Old Code
def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
'''

def n_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(n_sum(numbers, 2) == 20)
