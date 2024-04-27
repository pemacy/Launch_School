'''
Create a function that takes two string arguments and returns the number of
times that the second string occurs in the first string. Note that overlapping
strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.
'''

def count_substrings(s1, s2):
    # Problem
    #   Input
    #       function takes 2 string args
    #   Output
    #       returns an integer
    #   Rules
    #       integer returned is the number of times the second string occurs
    #           in the first string
    #       overlapping strings don't count
    #   Assumptions:
    #       seconds argument is never an empty string
    #   Edge Cases:
    #       1st arg empty string

    # Data Structure:
    #   working with strings
    #   need to remove s2 pattern from the string
    #   count how many times pattern can be removed

    # Algorithm
    #   initialize count to 0
    #   intialize start index to 0
    #   start infinite loop
    #   using the str.find() function, find the first occurance
    #   if find returns an index value
    #       add 1 to count
    #       add s2 length to start_index
    #   else
    #       break out of loop
    #   return count

    count = 0
    start_index = 0
    while True:
        idx_match = s1.find(s2, start_index)
        if idx_match != -1:
            count += 1
            start_index += idx_match + len(s2)
        else:
            break
    return count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
