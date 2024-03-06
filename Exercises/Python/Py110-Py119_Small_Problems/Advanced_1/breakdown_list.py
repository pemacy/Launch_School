def breakdown_list(lst):
    len_lst = len(lst)
    if len_lst == 1:
        return lst
    else:
        half_len = len_lst // 2
        return [breakdown_list(lst[:half_len]), breakdown_list(lst[half_len:])]

print(breakdown_list([1,2,3,4,5]))
