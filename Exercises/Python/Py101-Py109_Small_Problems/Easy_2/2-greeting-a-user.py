'''
Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).
'''

'''
What is your name? Sue
Hello Sue.
'''

'''
What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?
'''

def greet_user():
    name = input('What is your name? ')
    greeting = f'Hello {name}'
    if name[-1] == '!':
        print(greeting.upper() + 'WHY ARE YOU YELLING?')
    else:
        print(greeting)

greet_user()
