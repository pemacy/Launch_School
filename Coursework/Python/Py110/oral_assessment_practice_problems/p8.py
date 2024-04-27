'''
Create a function that takes a non-empty string as an argument. The string
consists entirely of lowercase alphabetic characters. The function should
return the length of the longest vowel substring. The vowels of interest are "
a", "e", "i", "o", and "u".
'''

def longest_vowel_substring(s):
    # Problem
    #   function takes non-empty string
    #   string has only lowercase characters
    #   returns the length of the longest vowel only substring

    # Data Structure:
    #   top_count integer
    #   current_count_integer

    # Algorithm:
    #   make vowel string 'aeiou'
    #   set top_count and current_count  integers to 0
    #   for e in string:
    #       if e in vowels:
    #           current_count += 1
    #       else:
    #           if current_count > total_count:
    #               total_count = current_count
    #           current_count = 0

    vowels = 'aeiou'
    current_count = 0
    top_count = 0

    for l in s:
        if l in vowels:
            current_count += 1
            top_count = max(top_count, current_count)
        else:
            top_count = max(top_count, current_count)
            current_count = 0


    return top_count

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
