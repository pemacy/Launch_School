'''
What does the last line in the following code output?
'''

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)


# it prints:
# [1,2]
# {'first': [1,2]}
