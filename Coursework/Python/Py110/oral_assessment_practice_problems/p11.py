'''
Create a function that takes a nonempty string as an argument and returns a
tuple consisting of a string and an integer. If we call the string argument s,
the string component of the returned tuple t, and the integer component of the
tuple k, then s, t, and k must be related to each other such that s == t * k.
The values of t and k should be the shortest possible substring and the
largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.
'''

def repeated_substring(s):
    # Problem
    #   Inputs: nonempty string
    #   Outputs: tuple of a string and an int (t, k)
    #   Rules:
    #       s == t * k
    #       ex: 'abcacb' = 'abc' * 2
    #
    #       t and k values should be shorted possible substring
    #         and longest possible repeat count

    # Data Structure:
    #   list to hold all possible substrings
    #   dictionary to hold substring: split counts

    # Algorithm:
    #   find all substrings and store in list
    #   send all substrings as split parameter
    #       if split returns with all empty strings it is a perfect substring
    #       store in dictionary with empty string count - 1
    #   return k:v pair of highest count

    substrings = []
    perfect_subs = {}
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    perfect_subs = { sub: len(s.split(sub)) - 1 for sub in substrings
                   if all([ el == '' for el in s.split(sub) ]) }
    max_count = max(perfect_subs.values())
    imax =  [ [sub, count] for sub, count in perfect_subs.items() if count == max_count ][0]
    return tuple(imax)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
