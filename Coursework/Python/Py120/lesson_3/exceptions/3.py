try:
    n1 = int(input('Enter number 1 >> '))
    n2 = int(input('Enter number 2 >> '))
    result = n1 // n2
except (ZeroDivisionError, ValueError) as e:
    print('An Error Has Occured')
    print(e)
else:
    print(F"the result is {result}")
finally:
    print('End of Program')
