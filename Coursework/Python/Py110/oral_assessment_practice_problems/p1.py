'''
Create a function that takes a list of numbers as an argument. For each numbe
r, determine how many numbers in the list are smaller than it, and place the
answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs
multiple times in the list, it should only be counted once.
'''

def smaller_numbers_than_current(lst):
    # iterate through each number number
    # count numbers it is greater than in the rest of the list
    # don't compare it with the same number twice
    # put the count in a separate list
    # return that list

    # data structure:   list to hold counts
    #                   set to loop through values

    compare_set = set(lst)
    count_lst = []
    for num in lst:
        count_lst.append(len([el for el in compare_set if el < num]))

    return count_lst


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
