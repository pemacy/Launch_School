'''
Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.
'''

def sum_square_difference(num):
    num_range = range(1, num + 1)
    square_sums = sum(num_range) ** 2
    sum_squares = sum([ n ** 2 for n in num_range ])
    return square_sums - sum_squares


print(sum_square_difference(3))      # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10))     # 2640
print(sum_square_difference(1))      # 0
print(sum_square_difference(100))    # 25164150
