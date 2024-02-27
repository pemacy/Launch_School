def remainder_3(numbers):
    return [ num if num % 3 == 0 else None for num in numbers ]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(remainder_3(numbers_1))
print(remainder_3(numbers_2))
print(remainder_3(numbers_3))
print(remainder_3(numbers_4))
