my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

len_1 = len(my_list)
counter_1 = 0

while counter_1 < len_1:
    counter_2 = 0
    arr = my_list[counter_1]
    len_2 = len(arr)
    while counter_2 < len_2:
        if arr[counter_2] % 2 == 0: print(arr[counter_2])
        counter_2 += 1
    counter_1 += 1
