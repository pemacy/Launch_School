'''
Write a function that takes a string, doubles every consonant character in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.
'''

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def double_consonants(s):
    return ''.join([ 2 * l if l.lower() in CONSONANTS else l for l in s ])

print(double_consonants('String'))          # "SSttrrinngg"
print(double_consonants('Hello-World!'))    # "HHellllo-WWorrlldd!"
print(double_consonants('July 4th'))        # "JJullyy 4tthh"
print(double_consonants(''))                # ""
