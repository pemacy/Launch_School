'''
Bubble Sort is one of the simplest sorting algorithms available. It is not an efficient algorithm, so developers rarely use it in real code. However, it is an excellent exercise for student developers. In this exercise, you will write a function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. On each pass, the two values of each pair of consecutive elements are compared. If the first value is greater than the second, the two elements are swapped. This process is repeated until a complete pass is made without performing any swaps. At that point, the list is completely sorted.
'''

def bubble_sort(lst):
    lst_len = len(lst)
    is_sorted = False
    while not is_sorted:
        touched = 0
        for i in range(1, lst_len):
            if lst[i] < lst[i-1]:
                touched = 1
                lst[i-1], lst[i] = lst[i], lst[i-1]
        if touched == 0: is_sorted = True

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1)    # [3, 5]

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2)    # [1, 2, 4, 6, 7]

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
bubble_sort(lst3)
print(lst3)    # ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]
