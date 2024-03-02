'''
Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.
'''

def center_of(s):
    if not s: return None

    # s = ''.join(s.split())

    s_len = len(s)
    if s_len % 2 == 0:
        ans = s[ s_len // 2 - 1 : s_len // 2 + 1 ]
        print(f'Length of {s} is {s_len}.  Middle of {s} is {ans}')
        return ans
    else:
        ans = s[ s_len // 2 ]
        print(f'Length of {s} is {s_len}.  Middle of {s} is {ans}')
        return ans


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
