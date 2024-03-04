'''
In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.
'''

num_to_string = __import__('10-convert-number-to-a-string')

def signed_integer_to_string(num):
    sign = '+' if num > 0 else '-'
    if num == 0: sign = ''
    num = abs(num)

    s = num_to_string.integer_to_string(num)
    return sign + s

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
