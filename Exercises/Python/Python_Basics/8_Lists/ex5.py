'''
Count the number of elements in scores that are 100 or above.
'''

scores = [96, 47, 113, 89, 100, 102]

count = 0

for el in scores:
    count += 1 if el >= 100 else 0

print(count)
