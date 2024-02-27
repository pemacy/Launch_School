def remainder_5(numbers):
    return [ num if num % 5 == 0 else None for num in numbers ]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(f'{numbers_1} % 5 = {remainder_5(numbers_1)}')
print(f'{numbers_2} % 5 = {remainder_5(numbers_2)}')
print(f'{numbers_3} % 5 = {remainder_5(numbers_3)}')
print(f'{numbers_4} % 5 = {remainder_5(numbers_4)}')
