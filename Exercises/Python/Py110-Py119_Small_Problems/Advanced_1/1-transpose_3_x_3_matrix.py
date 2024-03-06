'''
A 3x3 matrix can be represented by a list of nested lists: an outer list that contains three sub-lists that each contain three elements. For example, the 3x3 matrix shown below:
'''

def transpose(matrix):
    return [ list(arr) for arr in zip(matrix[0], matrix[1], matrix[2]) ]

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
