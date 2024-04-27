'''
Create a function that takes a list of integers as an argument. The function
should return the minimum sum of 5 consecutive numbers in the list. If the
list contains fewer than 5 elements, the function should return None.
'''

def minimum_sum(lst):
    # returns None if len list < 5
    # returns minimum sum of 5 consecutive integers in the list

    # data structure: list to store all sums

    # algorithm:
    #   determine number of 5-consecutive integers in list
    #       consecs = len lst - 5 + 1
    #   for i in range(0, consecs)
    #       slice lst into [i:i + 5]
    #       store sum of slice in all_sums
    #   find min_sum of all_sums list
    #   return min_sums

    if len(lst) < 5:
        return None
    num_consecs = len(lst) - 5 + 1
    all_sums = []
    for i in range(0, num_consecs):
        all_sums.append(sum(lst[i:i+5]))
    return min(all_sums)


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
