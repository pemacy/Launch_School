'''
In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion methods available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.
'''

str_to_num = __import__('8-convert-a-string-to-a-number')

def string_to_signed_integer(s):
    if s[0] in str_to_num.NUM_ARRAY:
        return str_to_num.string_to_integer(s)
    else:
        sign = -1 if s[0] == '-' else 1
        return sign * str_to_num.string_to_integer(s[1:])

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
