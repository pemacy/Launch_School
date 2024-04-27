'''
Create a function that takes an list of integers as an argument. Determine and
return the index N for which all numbers with an index less than N sum to the
same value as the numbers with an index greater than N. If there is no index
that would make this happen, return -1.

If you are given an list with multiple answers, return the index with the
smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the
numbers to the right of the last element is 0.
'''

def equal_sum_index(lst):
    # Problem:
    #   Input - list of integers
    #   Output - integer representing index N for which all numbers of index
    #           values less than N sum to the same value as the numbers with
    #           an index greater than N
    #           OR
    #           -1 if this condition does not exist
    #   Rules:
    #       all numbers of index values below N must sum to the same sum as
    #           all numbers of index values greater than N
    #       number at index N is excluded from either sum
    #       if multiple index "N"s existe, return the smallest index N
    #       sum of numbers to the left of index 0 is 0
    #       sum of numbers to the right of the last index is 0
    #   Assumptions:
    #       List argument will have only integers
    #       List argument will have at least one value
    #   Edge Cases:
    #       empty list
    #       zero
    #       incorrect type in list
    #       maximum capability

    # Data Structure:
    #   Dictionary of key = index, value = tuple of (left sum, right sum)

    # Algorithm:
    #   storage = {}
    #   storage[0] = (0, sum(lst))
    #   storage[len(lst) - 1] = (sum(lst), 0)
    #   for n in range(1, len(lst) - 1):
    #       sum_left = sum(lst[:i])
    #       sum_right = sum(lst[i+1:])
    #       storage[n] = (sum_left, sum_right)
    #   filtered_list = filter our all n numbers where sums are not equal
    #   if filtered_list empty:
    #       return -1
    #   return lowest n number in filtered_list

    d = {}
    d[0] = (0, sum(lst[1:]))
    d[len(lst) - 1] = (sum(lst[:len(lst)]), 0)
    for n in range(1, len(lst) - 1):
        sum_left = sum(lst[:n])
        sum_right = sum(lst[n + 1:])
        d[n] = (sum_left, sum_right)
    filtered_list = [ n for n, t in d.items() if t[0] == t[1] ]
    if len(filtered_list) == 0:
        return -1
    return filtered_list[0]

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)
