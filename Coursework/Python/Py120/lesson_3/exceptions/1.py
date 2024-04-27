try:
    n1 = int(input('Enter number 1 >> '))
    n2 = int(input('Enter number 2 >> '))
    result = n1 // n2
    print(F"the result is {result}")
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print('Value Error')
    print(e)
