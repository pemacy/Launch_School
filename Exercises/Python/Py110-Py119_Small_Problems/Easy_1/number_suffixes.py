import math

def find_suffix(num):
    match num % 10:
        case 1:
            suffix = 'st'
        case 2:
            suffix = 'nd'
        case 3:
            suffix = 'rd'
        case _:
            suffix = 'th'
    return suffix


def num_with_suffix(num):
    if num % 100 <= 20 and num % 100 >= 10:
        suffix = 'th'
    else:
        suffix = find_suffix(num)

    return f'{num}{suffix}'
