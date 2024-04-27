'''
Create a function that takes a single integer argument and returns the sum of
all the multiples of 7 or 11 that are less than the argument. If a number is a
multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21,
and 22. The sum of these multiples is 75.

If the argument is negative, return 0.
'''

def seven_eleven(num):
    # Problem
    #   Input: single integer
    #   Output: single integer - sum of all multiples of 7 and 11 less than num
    #   Rules:
    #       if number is multiple of both 7 and 11 count it once
    #       all numbers summed must be less than number argument passed
    #   Assumptions:
    #       argument passed will be an integer number
    #       argument passed will be > 0
    #   Edge Cases:

    # Data Structure:
    #   Set to hold all multiples of 7
    #   Set to hold all multiples of 11
    #   Union Set of both sets

    # Algorithm:
    #   range loop of multiples of 7 up to num passed, add numbers into
    #       mult_7 set
    #   range loop of multiples of 11 up to num passed, add numbers into
    #       mult_11 set
    #   all_mults union set = set_7 | set_11
    #   return sum(union_set)

    mult_7 = set()
    mult_11 = set()

    for n in range(7, num, 7):
        mult_7.add(n)

    for n in range(11, num, 11):
        mult_7.add(n)

    all_mults = mult_7 | mult_11

    return sum(all_mults)
# Examples
print(seven_eleven(25) == 75) # 7 + 11 + 14 + 21 + 22
print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
