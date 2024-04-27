'''
Create a function that takes two strings as arguments and returns True if some
portion of the characters in the first string can be rearranged to match the
characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic
characters. Neither string will be empty.
'''

def unscramble(s1, s2):
    # Problem
    #   Input: 2 string arguments
    #   Output: boolean True or False
    #   Rules:
    #       returns True if some portion of the first string can be re-arranged
    #           to match the characters in the second string
    #       otherwise False
    #   Assumptions:
    #       both string args contain lowercase alphabetic chars only
    #       no empty strings
    #   Edge Cases:
    #       None

    # Data Structure:
    #   list for characters in first string to pop

    # Algorithm
    #   make list of first string
    #   loop through each character of second string
    #       if char is in first string, pop it from first string list
    #       else return false
    #   return True if made it through whole loop

    s1_list = list(s1)
    for l in s2:
        try:
            idx = s1_list.index(l)
        except ValueError:
            return False
        s1_list.pop(idx)
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
