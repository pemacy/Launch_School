class NegativeNumberError(Exception):
    def __init__(self, message="Number can't be negative"):
        super().__init__(message)

n = int(input('Enter a Number: '))
if n < 0:
    raise NegativeNumberError(f'Number cannot be negative: {n}')
print(F"Number is: {n}")


