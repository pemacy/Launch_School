'''
Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.
'''

def running_total(l):
    return [ sum(l[:i+1]) for i, _ in enumerate(l) ]
    # lst = []
    # for i in range(1, len(l) + 1):
    #     lst.append(sum(l[:i]))
    # return lst


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
