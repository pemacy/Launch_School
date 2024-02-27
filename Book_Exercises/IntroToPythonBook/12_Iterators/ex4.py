my_list = [6, 3, 0, 11, 20, 4, 17]

length = len(my_list)
i = 0

print('Even Numbers')

while i < length:
    if my_list[i] % 2 == 0:
        print(my_list[i])
    i += 1

print('\n Odd Numbers')

for num in my_list:
    if num % 2 != 0:
        print(num)
