def multiply(n1, n2):
    result = float(n1) * float(n2)
    return result
num_1 = input('Enter first number: ')
num_2 = input('Enter second number: ')
print(f"{num_1} x {num_2} = {multiply(num_1, num_2):.2f}")
