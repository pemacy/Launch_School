'''
Write a function that returns the last element of a list provided as an argument. For example:
'''

def last(arr):
    if arr:
        l = len(arr)
        return arr[l - 1]
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
