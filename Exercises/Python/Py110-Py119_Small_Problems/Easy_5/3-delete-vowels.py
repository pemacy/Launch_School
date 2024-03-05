'''
Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.
'''

VOWELS = 'aeiouAEIOU'

def remove_vowels(lst):
    new_lst = []
    for word in lst:
        s = ''
        for letter in word:
            if letter in VOWELS:
                continue
            else:
                s += letter
        new_lst.append(s)

    return new_lst

print(remove_vowels(['abcdefghijklmnopqrstuvwxyz']))        # ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(['green', 'YELLOW', 'black', 'white'])) # ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(['ABC', 'AEIOU', 'XYZ']))               # ['BC', '', 'XYZ']
