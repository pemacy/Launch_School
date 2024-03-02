'''
Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.
'''

import math

def is_it_odd(num):
    num = int(num)

    if math.fabs(num) % 2 == 0:
        return False
    else:
        return True

# Tests
print(is_it_odd(1)) # True
print(is_it_odd(2)) # False
print(is_it_odd(0)) # False
