def find_integers(tup):
    arr = []
    for el in tup:
        if type(el) is int: arr.append(el)
    return arr

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
