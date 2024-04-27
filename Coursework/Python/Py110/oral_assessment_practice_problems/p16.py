'''
Create a function that returns the count of distinct case-insensitive
alphabetic characters and numeric digits that occur more than once in the
input string. You may assume that the input string contains only alphanumeric
characters.
'''

def distinct_multiples(s):
    # Problem
    #   Input: alphanumeric string
    #   Output: integer of count of distinct case insensitve characters and digits
    #               that occur more than once

    return len([ l for l in set(s.lower()) if s.lower().count(l) > 1 ])

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
