'''
Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.
'''

import math

def find_suffix(cent):
    match cent % 10:
        case 1:
            suffix = 'st'
        case 2:
            suffix = 'nd'
        case 3:
            suffix = 'rd'
        case _:
            suffix = 'th'
    return suffix


def century(year):
    cent = math.ceil(year / 100)

    if cent % 100 <= 20 and cent % 100 >= 10:
        suffix = 'th'
    else:
        suffix = find_suffix(cent)

    return f'{cent}{suffix}'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
