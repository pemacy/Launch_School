import random

highest = 10
# number = random.randrange(highest + 1)
# print(number)

while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break
