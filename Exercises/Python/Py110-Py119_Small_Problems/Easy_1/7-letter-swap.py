'''
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.
'''

def swap(s):
    swapped_s = []
    for w in s.split():
        l = list(w)
        l[0], l[-1] = [l[-1], l[0]]
        swapped_s.append(''.join(l))
    swapped_s = ' '.join(swapped_s)
    print(swapped_s)
    return swapped_s

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
