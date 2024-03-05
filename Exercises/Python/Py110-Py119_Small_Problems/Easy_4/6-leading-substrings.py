'''
Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.
'''

def leading_substrings(s):
    lst = []
    i = 1

    while i <= len(s):
        lst.append(s[:i])
        i += 1

    return lst

print(leading_substrings('abc'))      # ['a', 'ab', 'abc']
print(leading_substrings('a'))        # ['a']
print(leading_substrings('xyzzy'))    # ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']
