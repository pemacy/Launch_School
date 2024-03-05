'''
Write a function that takes a string, doubles every character in the string, and returns the result as a new string.
'''

def repeater(s):
    return ''.join([ 2 * l for l in s ])
    # s_repeat = ''

    # for l in s:
    #     s_repeat += 2 * l
    # return s_repeat

print(repeater('Hello'))        # "HHeelllloo"
print(repeater('Good job!'))    # "GGoooodd  jjoobb!!"
print(repeater(''))             # ""
