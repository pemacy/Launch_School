'''
Given a list of strings, return a new list where the strings are sorted based
on the highest number of adjacent consonants a string contains. If two strings
contain the same highest number of adjacent consonants, they should retain
their original order in relation to each other. Consonants are considered
adjacent if they are next to each other in the same word or if there is a
space between two consonants in adjacent words.

Tasks

You are provided with the problem description above. Your tasks for this step
are:

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.
'''

'''
Task 1: Understand the Problem
    Input: list of strings
    Output: new list where strings are sorted based on highest number of
            adjacent consonants a string contains
    Rules:
        Sort order is by highest number of adjacent consonants
        If 2 strings have the same amount they should preserve original order
        Adjacency is kept even if there is a space between words

    Questions:
        Can you mutate the input list
'''

'''
Task 2: Examples

print(sort_adjacents(['this is the first', 'gggggaaa', seccc]) == ['ggggggaaa', 'this is the first', seccc])
print(sort_adjacents(['split space ttttt ttt', 'no split space tttttttt']) == ['no split space tttttttt', 'split space ttttt ttt'])
'''

'''
Task 3: Data Structure

Dictionary:
    where the keys are the number of consecutive consonants
    values are lists containing the strings that fall into that count
'''

'''
Task 4: Algorithm

sort_consonants(list):
    create result list
    loop through input list
        initialize consonant count to 0
        count consonants
        append string to dictionary key of that consonant count

    result = concatonate dictionary values together, starting from the highest key down
    return result

count_consonants(string):
    lowercase = 'bcdfghjklmnpqrstvwxyz'
    uppercase = 'bcdfghjklmnpqrstvwxyz'.upper()
    all_consonants = lowercase + uppercase

    total_count = 0
    count = 0
    loop through string:
        if char is in all_consolants:
            count += 1
        else:
            if count > total_count:
                total_count = count
            count = 0
    return total_count

concat_dict_values(dict):
    descending_keys = sorted(list(dict.keys()), reverse=True)
    result = []
    for key in descending_keys:
        result += dict[key]
    return result
'''

def sort_consonants(lst):
    consonant_count_dict = {}
    for str_ in lst:
        str_consonant_count = count_consonants(str_)
        consonant_count_dict.setdefault(str_consonant_count, [])
        consonant_count_dict[str_consonant_count].append(str_)

    result = concat_dict_values(consonant_count_dict)
    return result

def count_consonants(str_):
    lowercase = 'bcdfghjklmnpqrstvwxyz'
    uppercase = 'bcdfghjklmnpqrstvwxyz'.upper()
    all_consonants = lowercase + uppercase

    total_count = 0
    count = 0
    for c in str_:
        if c.isspace():
            continue
        elif c in all_consonants:
            count += 1
        else:
            if count > total_count:
                total_count = count
            count = 0

    if count > total_count:
        total_count = count
    return total_count

def concat_dict_values(d):
    descending_keys = sorted(list(d.keys()), reverse=True)
    result = []
    for key in descending_keys:
        result += d[key]
    return result

# my_list = ['this is the first', 'gggggaaa', 'seccc']
# my_result = ['gggggaaa', 'this is the first', 'seccc']
# print(sort_consonants(my_list) == my_result)

# my_list = ['split space ttttt ttt', 'no split space tttttttt']
# my_result = ['no split space tttttttt', 'split space ttttt ttt']
# print(sort_consonants(my_list) == my_result)

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_consonants(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_consonants(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_consonants(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_consonants(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_consonants(my_list))
# ['xxxx', 'xxxb', 'xxxa']
