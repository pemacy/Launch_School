n = int(input('Enter a Number: '))
if n < 0:
    raise ValueError(f'Number cannot be negative: {n}')
print(F"Number is: {n}")
