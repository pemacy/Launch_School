my_list = [
    1, 3, 6, 11,
    4, 2, 4,
    9, 17, 16, 0,
]

new_list = []

for el in my_list:
    new_list.append('even') if el % 2 == 0 else new_list.append('odd')

print(new_list)
