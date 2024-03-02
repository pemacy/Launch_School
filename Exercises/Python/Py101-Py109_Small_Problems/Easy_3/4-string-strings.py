'''
Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.
'''

def stringy(num):
    s_bin = ''
    for el in range(num):
        if el % 2 == 0:
            s_bin += '1'
        else:
            s_bin += '0'
    return s_bin


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
