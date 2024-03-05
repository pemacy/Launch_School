'''
You want to multiply all elements of a list by 2. However, the function is not returning the expected result.
'''

'''
Original Code
def multiply_list(lst):
    for item in lst:
        item *= 2
    return lst

print(multiply_list([1, 2, 3]))
'''

'''
This code does not work because even though item and the corresponding lst[] element reference the same value, you are re-assigning 'item' to a new value, but not re-assigning the lst[] element
In order to change the lst, you must either create a new list and fill it with the processed elements, or re-assign the elements of the orginal list to the duplicated values:
'''

def multiply_list(lst):
    for idx, item in enumerate(lst):
        lst[idx] = item * 2
    return lst

print(multiply_list([1, 2, 3]))
