'''
Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

Numerical score letter grade list:

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'
Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.
'''

def average(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def get_grade(n1, n2, n3):
    ave = average(n1, n2, n3)
    print(ave)

    if ave >= 90:
        return 'A'
    elif ave >= 80:
        return 'B'
    elif ave >= 70:
        return 'C'
    elif ave >= 60:
        return 'D'
    else:
        return 'F'


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
