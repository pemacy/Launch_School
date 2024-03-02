'''
Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.
'''

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for el in numbers:
    print(f'A {el} number is {numbers[el]}')
