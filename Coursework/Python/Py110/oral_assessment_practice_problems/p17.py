'''
Create a function that takes a list of integers as an argument. The function
should determine the minimum integer value that can be appended to the list so
the sum of all the elements equal the closest prime number that is greater
than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum
to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the
list to sum to 7.
'''

from math import sqrt

def nearest_prime_sum(lst):
    # Problem
    #   Input - list of integers
    #   Output - integer: min int that can be appended to the list so the sum
    #                     of all the elements equals the closest prime number
    #                     greater than the current sum
    #   Rules:
    #       sum of new list must be greater than current sum
    #       new sum must be prime
    #       new sum must be the next availalbe prime
    #   Assumptions:
    #       non empty list
    #       only integers in the list
    #       non-negative numbers
    #   Edge Cases:
    #       emptiness
    #       zero
    #       negatives
    #       maximum capabilities

    # Data Structure
    #   integer to hold current sum
    #   counter starting at 1 to add to current sum

    # Algorithm:
    #   endless loop
    #       while sum + counter != prime
    #           counter += 1
    #   test for prime:
    #       for i in range(3, sqrt(num)):
    #           if num % i == 0
    #               prime == True

    lst_sum = sum(lst)
    counter = 1
    while True:
        prime_sum = lst_sum + counter
        if prime_sum % 2 == 0 or \
           any([ prime_sum % i == 0
                for i in range(3, int(sqrt(prime_sum)) + 1, 2) ]):
            counter += 1
        else:
            break
    return prime_sum - lst_sum

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
