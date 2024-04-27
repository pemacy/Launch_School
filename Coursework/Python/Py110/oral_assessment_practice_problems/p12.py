'''
Create a function that takes a string as an argument and returns True if the
string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least onc
e. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a
pangram since it uses every letter at least once. Note that case is irrelevant.
'''

def is_pangram(s):
    # Problem:
    #   Input: string
    #   Output: True or False
    #   Rules:
    #       returns True if the string is pangram, or False otherwise
    #       pangrams contain every letter of the alphabet at least once
    #       doesn't care about non-alpha letters
    #   Assumptions:
    #       a non-empty string will be the input
    #   Edge Cases:
    #       None

    # Data Structure: string holding a-z and A-Z
    #                   a new string of s with all non letters removed

    # Algorithm:
    #   loop through each letter and test if it's in abc string
    #   if any False return False, otherwise return True
    abc = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()

    return all([ l in s for l in abc ])

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
