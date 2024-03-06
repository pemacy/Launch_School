'''
A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201.
'''

def has_no_duplicate(num):
    # print(f'{sorted(list(str(num)))} == {sorted(list((set(str(num)))))}')
    return sorted(list(str(num))) == sorted(list(set(str(num))))

def featured(num):
    count = num

    while True:
        count += 1
        if (count % 7 == 0) and (count % 2 != 0) and (has_no_duplicate(count) == True):
            return count
        elif count > 9876543201:
            return 'No featured number available'


print(featured(12))           # 21
print(featured(20))           # 21
print(featured(21))           # 35
print(featured(997))          # 1029
print(featured(1029))         # 1043
print(featured(999999))       # 1023547
print(featured(999999987))    # 1023456987
print(featured(9876543186))   # 9876543201
print(featured(9876543200))   # 9876543201
print(featured(9876543201))   # "There is no possible number that fulfills those requirements."
