'''
A triangle is classified as follows:

Equilateral: All three sides are of equal length.
Isosceles: Two sides are of equal length, while the third is different.
Scalene: All three sides are of different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.
'''

def triangle(s1, s2, s3):
    if s1 == 0 or s2 == 0 or s3 == 0:
        return 'invalid'
    elif (s1 + s2 < s3) or (s1 + s3 < s2) or (s2 + s3 < s1):
        return 'invalid'
    elif (s1 == s2) and (s2 == s3) and (s1 == s3):
        return 'equilateral'
    elif (s1 == s2) or (s2 == s3) or (s1 == s3):
        return 'isosceles'
    else:
        return 'scalene'


print(triangle(3, 3, 3))        # "equilateral"
print(triangle(3, 3, 1.5))     # "isosceles"
print(triangle(3, 4, 5))       # "scalene"
print(triangle(0, 3, 3))       # "invalid"
print(triangle(3, 1, 1))       # "invalid"
