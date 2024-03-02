'''
Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.

For simplicity, this exercise assumes that the Gregorian calendar has been in continuous use since since the year 1. We'll address that assumption in the next exercise that follows this one.

To determine whether a given year is a leap year, use the rules of the Gregorian calendar:

If the year is divisible by 400, it is a leap year.
If the year is divisible by 100 but not by 400, it is not a leap year.
If the year is divisible by 4 but not by 100, it is a leap year.
All other years are not leap years.
'''

def div_400_true(num):
    return num % 400 == 0

def div_100_true(num):
    return num % 100 == 0

def div_4_true(num):
    return num % 4 == 0

def is_leap_year(num):
    if div_400_true(num):
        return True
    elif div_4_true(num) and not div_100_true(num):
        return True
    else:
        return False

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
