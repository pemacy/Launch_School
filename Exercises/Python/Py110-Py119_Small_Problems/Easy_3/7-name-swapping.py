'''
Write a function that takes a string argument consisting of a first name, a space, and a last name, and returns a new string consisting of the last name, a comma, a space, and the first name.
'''

def swap_name(name):
    return ', '.join(name.split()[::-1])

print(swap_name('Joe Roberts'))    # "Roberts, Joe"
