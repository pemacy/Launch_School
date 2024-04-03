'''
1. numbers = [1, 2, 3, 4]
    numbers.clear()
    while numbers:
        numbers.pop()

2. print([1, 2, 3] + [4, 5])
    # this will output [1,2,3,4,5]

3.  str1 = "hello there"
    str2 = str1
    str2 = "goodbye!"
    print(str1)

    # this will output "hello there"

4.  my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
    my_list2 = my_list1.copy()
    my_list2[0]['first'] = 42
    print(my_list1)

    # This will output 42 for the value of 'first'

5. def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

    # re-write so it doesn't use True or False:
        def is_color_valid(color):
            return color == "blue" or color == "green":
'''
