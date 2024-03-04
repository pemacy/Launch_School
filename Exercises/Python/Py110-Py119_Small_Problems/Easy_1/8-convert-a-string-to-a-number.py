'''
Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion methods available in Python, such as int. Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.
'''

NUM_ARRAY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def string_to_integer(s):
    s_len = len(s) - 1
    n = 0
    for l in s:
        n += (10 ** s_len) * NUM_ARRAY.index(l)
        s_len -= 1
    return n

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True
