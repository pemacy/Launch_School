'''
Check whether the keys 'name' and 'grade' exist in the following dictionary:
'''

student = {
    'id': 123,
    'grade': 'B',
}

def key_exists_q(lst, key):
    return key in lst.keys()

print(key_exists_q(student, 'grade'))
print(key_exists_q(student, 'name'))


# easier way

print('grade' in student)
print('name' in student)
