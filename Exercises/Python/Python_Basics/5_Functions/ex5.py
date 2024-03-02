'''
Without running the following code, determine what it will print:
    # <function multiples_of_three at 0x32210...>
'''

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

print(multiples_of_three)
