num = 4936
count = 3

print(f'num = {num}')

while count >= 0:
    dig = num // 10**count
    num = num - (dig * 10**count)
    count -= 1
    print(dig)

