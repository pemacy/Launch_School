'''
Create a function that takes a string argument and returns a dict object in
which the keys represent the lowercase letters in the string, and the values
represent how often the corresponding letter occurs in the string.
'''

def count_letters(s):
    # Problem
    # takes a string object
    # returns a dict object
    #   key represetns lowercase letters in the string
    #   values represent count of corresponding letter in the string
    #   non-letters do not get counted

    # Data Structure
    # dictionary

    # Algorithm
    # create empty dictionary
    # loop through set of letters
    # store count in dict key of letter
    # return dictionary

    return { l: s.count(l) for l in set(s) if l.isalpha() and l.islower() }

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
