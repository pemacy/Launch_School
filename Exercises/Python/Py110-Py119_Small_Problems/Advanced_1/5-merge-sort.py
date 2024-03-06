'''
Merge sort is a recursive sorting algorithm that works by breaking down a list's elements into nested sublists, then combining those nested sublists back together in sorted order. It is best explained with an example. Given the list [9, 5, 7, 1], let's walk through the process of sorting it with merge sort. We'll start off by breaking the list down into nested sublists:

    [9, 5, 7, 1] -->
    [[9, 5], [7, 1]] -->
    [[[9], [5]], [[7], [1]]]

    [[[9], [5]], [[7], [1]]] -->
    [[5, 9], [1, 7]] -->
    [1, 5, 7, 9]

Write a function that takes a list argument and returns a new list that contains the values from the input list in sorted order. The function should sort the list using the merge sort algorithm as described above. You may assume that every element of the list will be of the same data type—either all numbers or all strings.

Feel free to use the merge function you wrote in the previous exercise.
'''

merge = __import__('4-merge-sorted-list')

def breakdown_list(lst):
    len_lst = len(lst)
    if len_lst == 1:
        return lst
    else:
        half_len = len_lst // 2
        return [breakdown_list(lst[:half_len]), breakdown_list(lst[half_len:])]

def merge_sort(lst):
    len_lst = len(lst)
    if len_lst == 1:
        return lst
    elif len_lst == 2:
        # print(lst)
        if type(lst[0]) != list: lst[0] = [lst[0]]
        if type(lst[1]) != list: lst[1] = [lst[1]]
        return merge.merge(lst[0], lst[1])
    else:
        # print(lst)
        half_len = len_lst // 2
        return merge_sort([merge_sort(lst[:half_len]), merge_sort(lst[half_len:])])

print(merge_sort([9, 5, 7, 1]))           # [1, 5, 7, 9]
print(merge_sort([5, 3]))                 # [3, 5]
print(merge_sort([6, 2, 7, 1, 4]))        # [1, 2, 4, 6, 7]

print(merge_sort(['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']))
# # ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]

print(merge_sort([7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]))
# # [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]
