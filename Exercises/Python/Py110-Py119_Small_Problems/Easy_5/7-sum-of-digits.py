'''
Write a function that takes one argument, a positive integer, and returns the sum of its digits.
'''

def sum_digits(num):
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num //= 10
    return sum_num

print(sum_digits(23))           # 5
print(sum_digits(496))          # 19
print(sum_digits(123456789))    # 45
