'''
scratch file for exam problems to try
'''

# friends1 = ['Rachel', 'Phoebe', 'Joey', 'Monica', 'Ross', 'Chandler']
# friends2 = friends1

# print(id(friends1) == id(friends2))

# friends1.reverse()

# print(friends1) # ?
# print(friends2) # ?
# print(friends2[0]) # ?

# num = 1

# def modify():
#     num += 1
#     print(num)

# modify()

# a = 3

# def foo():
#     b = 2
#     while a > b:
#         c = 3
#         b += 1

# foo()

# everest = "Everest"
# kilimanjaro = "Kilimanjaro"
# fuji = "Fuji"

# mountain_list = [everest, kilimanjaro, fuji]
# print(id(everest) == id(mountain_list[0]))

# for idx in range(len(mountain_list)):
#     mountain_list[idx] += " " + str(len(mountain_list[idx]))

# print(mountain_list)  # ['Everest 7', 'Kilimanjaro 11', 'Fuji 4']
# print(everest)
# print(kilimanjaro)
# print(fuji)

bar = 0
foo = ['']
baz = 3
qux = (bar > baz) or bar and baz or foo

print(qux)

'''
If we change the variable of `bar` to `4` for instance, the resultant value of
`qux` is `True`, which is the result of the first `or` operation `(bar > ba
z)`, which would seem to make the it the first evaluation.
'''

# if qux:
#     print("Operation succeeded")
# else:
#     print("Operation failed")

# name = 'Tom'

# def hi_name():
#     name = 'Barry'
#     print(f'Hi {name}!')

# hi_name() # outputs "Hi Barry!"


# def mutating_delete(lst):
#     lst.pop(-1)
#     return lst

# def non_mutating_delete(lst):
#     return lst[:-1]

# lst = [1, 2, 3]

# print(mutating_delete(lst) == [1, 2]) #=> True
# print(lst == [1, 2]) #=> True

# lst = [1, 2, 3]

# print(non_mutating_delete(lst) == [1, 2]) #=> True
# print(lst == [1, 2, 3]) #=> True
