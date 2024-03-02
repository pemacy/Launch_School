'''
Initialize a variable weather with a string value being 'sunny', 'rainy', or whatever weather condition you choose. Then, write an if statement that prints:

It's a beautiful day! if weather's value is 'sunny'
Grab your umbrella. if weather's value is 'rainy'
Let's stay inside. if weather's value is anything else
Test your code with different values for weather.
'''

import random


weather = ['sunny', 'rainy', 'snowy']
random_number = 0

while random_number != 2:
    random_number = random.randint(0, 2)
    match weather[random_number]:
        case 'sunny':
            print("It's a beautiful day!")
        case 'rainy':
            print("It's a rainy day!")
        case _:
            print("Let's stay inside")
