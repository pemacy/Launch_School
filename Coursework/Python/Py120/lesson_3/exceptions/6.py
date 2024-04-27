def inverse(lst):
    inv_lst = []
    for el in lst:
        try:
            inv = 1 / el
        except ZeroDivisionError as e:
            print("Can't divide by zero")
        except TypeError as e:
            print("List values must be numbers")
        except ValueError as e:
            print("Would this even happen?")
        else:
            inv_lst.append(inv)
    return inv_lst

print(inverse([1,2,3,4,5]))
print(inverse([1,2,0]))
print(inverse([1,2,'a']))
