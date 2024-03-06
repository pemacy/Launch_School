'''
Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in sorted order.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.
'''

def merge(l1, l2):
    if len(l1) == 0 or len(l2) == 0: return l1 + l2
    l1_copy = l1[:]
    l2_copy = l2[:]

    new_lst = []
    while len(l1_copy) > 0 and len(l2_copy) > 0:
        if l1_copy[0] <= l2_copy[0]:
            new_lst.append(l1_copy.pop(0))
        else:
            new_lst.append(l2_copy.pop(0))

    return new_lst + l1_copy + l2_copy


# print(merge([1, 5, 9], [2, 6, 8]))      # [1, 2, 5, 6, 8, 9]
# print(merge([1, 1, 3], [2, 2]))         # [1, 1, 2, 2, 3]
# print(merge([], [1, 4, 5]))             # [1, 4, 5]
# print(merge([1, 4, 5], []))             # [1, 4, 5]
