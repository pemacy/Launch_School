'''
Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:
'''

def substrings(s):
    ref_i = 0
    lst = []

    while ref_i < len(s):
        i = ref_i + 1
        while i <= len(s):
            lst.append(s[ref_i:i])
            i += 1
        ref_i += 1

    return lst

print(substrings('abcde'))

# prints
# [ "a", "ab", "abc", "abcd", "abcde",
#  "b", "bc", "bcd", "bcde",
#  "c", "cd", "cde",
#  "d", "de",
#  "e" ]
