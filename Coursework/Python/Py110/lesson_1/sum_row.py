"""
Imagine a sequence of consectutive even integers beginning with 2. The integers
are grouped in rows where the first row has 1 integer, the second row has 2
integers and so on.  Given an integer that represents the number of the row,
return the sum of the integers in that row
"""

def sum_rows(user_row):
    rows_dict = {}
    row = 1
    start = 2
    while row <= user_row:
        end = start + (2 * row)
        row_list = list(range(start, end, 2))
        rows_dict[row] = row_list
        row += 1
        start = end
    return sum(rows_dict[user_row])

print(sum_rows(1) == 2)
print(sum_rows(2) == 10)
print(sum_rows(5) == 130)
