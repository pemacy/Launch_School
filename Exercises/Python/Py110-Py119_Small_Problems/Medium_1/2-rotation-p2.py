'''
Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.
'''

rotate_p1 = __import__('1-rotation-p1')

def rotate_rightmost_digits(num, count):
    s_num = str(num)
    l_num = list(s_num)
    # take unaffected elements: l_num[0:len(l_num) - count]
    # add that to rotated end elements: rotate(l_num[len(l_num) - count:])
    pivot = len(l_num) - count
    l_num = l_num[:pivot] + rotate_p1.rotate_list(l_num[pivot:])
    return(int(''.join(l_num)))

"""
print(rotate_rightmost_digits(735291, 2))      # 735219
print(rotate_rightmost_digits(735291, 3))      # 735912
print(rotate_rightmost_digits(735291, 1))      # 735291
print(rotate_rightmost_digits(735291, 4))      # 732915
print(rotate_rightmost_digits(735291, 5))      # 752913
print(rotate_rightmost_digits(735291, 6))      # 352917
"""
