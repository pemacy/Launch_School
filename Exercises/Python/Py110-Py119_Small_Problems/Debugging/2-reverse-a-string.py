'''
You have a function that should reverse a given string. However, it's not producing the expected output.
'''

'''
Original Code
def reverse_string(s):
    for char in s:
        s = char + s
    return s

print(reverse_string("hello"))
'''

'''
Orignal code won't work because it is adding to the string value that was passed
You need to create a new string variable, set it to an empty string, and add the chars to that
Then return the new string variable
'''

def reverse_string(s):
    rev_s = ''
    for char in s:
        rev_s = char + rev_s
    return rev_s

print(reverse_string("hello"))
