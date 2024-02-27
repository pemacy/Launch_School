my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# 1. my_list and another_list are equal
print(my_list == another_list) # => True
# 2. the lists assigned to my_list and another_list are not the same object
print(my_list is another_list) # => False
# 3. The nested lists at my_list[3] and another_list[3] are equal
print(my_list[3] == another_list[3]) # => True
# 4. The nested lists at element 3 ARE the same object
print(my_list[3] is another_list[3]) # => True
