'''
Medium 1 problem 2
'''

def factors(number):
    '''
    Practice
    '''
    divisor = number
    result = []
    # while divisor != 0:
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# number % divisor gives the remainder, so if there is no remainder
# it is a factor of that number
