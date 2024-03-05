'''
Our countdown to launch isn't behaving as expected. Why? Change the code so that our program successfully counts down from 10 to 1.
'''

'''
Original code:
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease(counter)

print('LAUNCH!')
'''

'''
The code doesn't run because 'counter' in the decrease function is a local variable
You can't reference a global variable if it is being shadowed by a parameter in the function definition
So you have to remove the parameter from the function def AND add global for the variable declaration in the function
Then the variable will reference the 'counter' variable in the global scope
'''

def decrease():
    global counter
    counter -= 1

counter = 10

for _ in range(10):
    print(counter)
    decrease()

print('LAUNCH!')
