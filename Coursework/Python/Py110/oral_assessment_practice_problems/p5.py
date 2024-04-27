'''
Create a function that takes a string argument and returns the character that
occurs most often in the string. If there are multiple characters with the
same greatest frequency, return the one that appears first in the string. When
counting characters, consider uppercase and lowercase versions to be the same.
'''

def most_common_char(s):
    # Problem
    # takes a string argument
    # returns a string of the character that occurs most often
    # if multiple characters have the same count, returns the first
    # case does not matter

    # Data Structure: nested dictionary {char: {count: c, order: o}}

    # Algorithm:
    #   loop through all letters with enumerate
    #   setdefault [letter] to dictionary
    #   count number of occurances
    #   set [letter][count] to count
    #   set [letter][order] to index

    # find max counts and letters that have that count
    # find order of each letter of max counts and return the letter with the lowest order

    s = s.casefold()
    storage = {}
    for l in s:
        if storage.get(l):
            continue
        storage[l] = s.count(l)
    max_count = max(storage.values())
    letters = [ l for l, count in storage.items() if count == max_count ]

    return letters[0]

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
