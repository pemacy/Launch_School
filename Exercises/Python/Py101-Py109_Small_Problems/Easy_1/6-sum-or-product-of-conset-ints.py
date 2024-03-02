'''
Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.
'''

'''
Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.
'''

'''
Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.
'''

def sum_it(num):
    answer = 0
    for el in range(1, num + 1):
        answer += el
    print(f'The sum of integers between 1 and {num} is {answer}')

def product_it(num):
    answer = 1
    for el in range(1, num + 1):
        answer *= el
    print(f'The product of integers between 1 and {num} is {answer}')

def consect_int_math():
    num = int(input('Please enter an integer greater than 0: '))
    op = input('Enter "s" to compute the sum, or "p" to compute the product: ')
    sum_it(num ) if op == 's' else product_it(num)

consect_int_math()
