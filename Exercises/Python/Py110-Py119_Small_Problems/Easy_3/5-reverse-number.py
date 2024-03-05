'''
Write a function that takes a positive integer as an argument and returns that number with its digits reversed.
'''

def reverse_number(num):
    return int(''.join(list(str(num))[::-1]))

print(reverse_number(12345))    # 54321
print(reverse_number(12213))    # 31221
print(reverse_number(456))      # 654
print(reverse_number(12000))    # 21 # Note that leading zeros in the result get dropped!
print(reverse_number(1))        # 1
