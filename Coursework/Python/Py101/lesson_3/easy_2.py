'''
1. numbers = [1,2,3,4,5]
    reversing the list without mutating:
        numbers[::-1], sorted(numbers, reverse=True), list(reversed(numbers))

2. numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]
    number1 = 8  # False
    number2 = 95 # True

    # determine if number1 and number2 are in numbers

    numbers.count(number1) > 0
    number1 in numbers
    numbers.count(number2) > 0
    number2 in numbers

3. # determin if 42, 100, and 101 are in 10-100 inclusive
    42 in range(10,101)
    100 in range(10,101)
    101 in range(10,101)

4. numbers = [1,2,3,4,5]
    # remove at index 2
    numbers.pop(2)
    del numbers[2]

5.  numbers = [1, 2, 3, 4]
    table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
    # verify if table and numbers are of type list:
        type(numbers) is list
        type(table) is list
        isinstance(numbers, list)
        isinstance(table, list)

6. title = "Flintstone Family Members"
    # center title on 40 char line:
        title.center(40, ' ')

7.  statement1 = "The Flintstones Rock!"
    statement2 = "Easy come, easy go."

        statement1.count('t')
        statement2.count('t')

8. ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
    ages.get('Spot') is not None
    'Spot' in ages

9. ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
    additional_ages = {'Marilyn': 22, 'Spot': 237}
    ages.update(additional_ages)
'''
