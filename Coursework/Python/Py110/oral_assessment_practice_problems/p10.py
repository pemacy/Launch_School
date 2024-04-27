'''
Create a function that takes a string of digits as an argument and returns the
number of even-numbered substrings that can be formed. For example, in the
case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '3
2', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a
separate substring.
'''

def even_substrings(s):
    # Problem
    #   Input: String
    #   Output: integer
    #   Rules:
    #       output is number of even-numbered substrings that can be formed
    #       even numbered substrings are all substrings of the string that
    #           end with an even number
    #       substrings do not have to be unique
    #   Assumptions:
    #       argument will be a string of only integers
    #   Edge Cases:
    #       empty string should return 0

    # Data Structure:
    #   list to hold all substrings of the string

    # Algorithm
    #   2 loops - one to loop over all indexes
    #               one to loop over start index to the end
    #   substrings = []
    #   for i in range(len(s)):
    #       for j in range(i + 1, len(s)):
    #           substrings.append(s[i:j])
    #
    #   comprehension to capture only even substrings
    #   even_substrings = [ sub_s for sub_s in substrings if int(sub_s) % 2 == 0 ]
    #   return len(even_substrings)

    substrings = []
    s_len = len(s) + 1
    for i in range(s_len):
        for j in range(i + 1, s_len):
            substrings.append(s[i:j])
    even_subs = [ sub_s for sub_s in substrings if int(sub_s) % 2 == 0 ]
    return len(even_subs)



print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
