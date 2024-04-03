'''
Comprehensions Practice Problems
'''

'''
1.
Consider the following nested dictionary:
'''

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

'''
Compute and display the total age of the family's male members. Try working
out the answer two ways: first with an ordinary loop, then with a
comprehension.

The result should be 444.
'''

print(sum([value['age'] for value in munsters.values()
           if value['gender'] == 'male']))

'''
2.
Given the following data structure, return a new list with the same structure,
but with the values in each sublist ordered in ascending order. Use a
comprehension if you can. (Try using a for loop first.)
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

print([sorted(sub_lst) for sub_lst in lst])

# expected results
[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# The string values should be sorted as strings, while the numeric values
# should be sorted as numbers.

'''
3.
Given the following data structure, return a new list with the same structure,
but with the values in each sublist ordered in ascending order as strings
(that is, the numbers should be treated as strings). Use a comprehension if
you can. (Try using a for loop first.)
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# for loop
sorted_lst = []
for l1 in lst:
    new_l1 = l1[:]
    new_l1.sort(key=str)
    sorted_lst.append(new_l1)

print(sorted_lst)

transform = [ sorted(l1, key = str) for l1 in lst ]
print(transform)

# expected results
result = [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
print(transform == result)

'''
Given the following data structure, write some code that defines a dictionary
where the key is the first item in each sublist, and the value is the second.
'''

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

transform = { l[0]: l[1] for l in lst }

# expected result
# Pretty printed for clarity
result =    {
                'a': 1,
                'b': 'two',
                'sea': {'c': 3},
                'D': ['a', 'b', 'c']
            }

print(transform == result)

'''
5.
Given the following data structure, sort the list so that the sub-lists are
ordered based on the sum of the odd numbers that they contain. You shouldn't
mutate the original list.
'''

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odds(arr):
    return sum([ el for el in arr if el % 2 != 0 ])

transform = sorted(lst, key = sum_odds)

'''
Note that the first sublist has the odd numbers 1 and 7; the second sublist
has odd numbers 1, 5, and 3; and the third sublist has 1 and 3. Since (1 + 3)
< (1 + 7) < (1 + 5 + 3), the sorted list should look like this:
'''

result = [[1, 8, 3], [1, 6, 7], [1, 5, 3]]
print(transform == result)

'''
6.
Given the following data structure, return a new list identical in structure
to the original but, with each number incremented by 1. Do not modify the
original data structure. Use a comprehension.
'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

transform = [ { k: v + 1 for k, v in h.items() } for h in lst ]

result = [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
print(transform == result)

'''
7.
Given the following data structure return a new list identical in structure to
the original, but containing only the numbers that are multiples of 3.
'''

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

transform = [ [ el for el in l1 if el % 3 == 0 ] for l1 in lst ]

result = [[], [3, 12], [9], [15, 18]]
print(result == transform)

'''
8.
Given the following data structure, write some code to return a list that
contains the colors of the fruits and the sizes of the vegetables. The sizes
should be uppercase, and the colors should be capitalized.
'''

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform_item(item):
    if item['type'] == 'fruit':
        return [ el.capitalize() for el in item['colors'] ]
    else:
        return item['size'].upper()

transform = [ transform_item(item) for item in dict1.values() ]
print(transform)

result = [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

'''
9.
This problem may prove challenging. Try it, but don't stress about it. If you
don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return a list that
contains only the dictionaries where all the numbers are even.
'''

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

transform = [ h for h in lst
             if all([ el % 2 == 0
                     for l1 in list(h.values())
                     for el in l1 ]) ]
print(transform)

result = [{'e': [8], 'f': [6, 10]}]

'''
10.
A UUID (Universally Unique Identifier) is a type of identifier often used to
uniquely identify items, even when some of those items were created on a
different server or by a different application. That is, without any
synchronization, two or more computer systems can create new items and label
them with a UUID with no significant risk of stepping on each other's toes. It
accomplishes this feat through massive randomization. The number of possible
UUID values is approximately 3.4 X 10E38, which is a huge number. The chance
of a conflict, a "collision", is vanishingly small with such a large number of
possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the
letters a-f) represented as a string. The value is typically broken into 5
sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa9
1'.

Note that our description of UUIDs is a simplified description of how UUIDs
are formed. There are several UUID versions, each with some non-random
characteristics in some of the bits. These different versions can play a part
in certain applications.
Write a function that takes no arguments and returns a string that contains a
UUID.
'''

import random

def uuid():
    chars = '0123456789abcdef'
    segments = [8, 4, 4, 4, 12]
    uuid_str = ''
    for segment in segments:
        seq = [ random.choice(chars) for _ in range(segment) ]
        uuid_str += ''.join(seq)
        if segment != 12:
            uuid_str += '-'
    return uuid_str

print(uuid())

'''
11.
The following dictionary has list values that contains strings. Write some
code to create a list of every vowel (a, e, i, o, u) that appears in the
contained strings, then print it.
'''

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

vowels = 'aeiou'

result = [ l for arr in dict1.values()
             for word in arr
             for l in word if l in vowels]

print(result)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

'''
Start by trying to write this using nested loops.

Extra Challenge: Once your nested loop code works, try to refactor the code so
it uses a single list comprehension. (You can print the resulting list outside
of the comprehension.)
'''
