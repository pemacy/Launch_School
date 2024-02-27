# does 3 appear in lists?

def three_in_lists(var_list):
    print(f'3 in the list {var_list}?: {3 in var_list}')

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

three_in_lists(numbers1)
three_in_lists(numbers2)
three_in_lists(numbers3)
three_in_lists(numbers4)
three_in_lists(numbers5)
