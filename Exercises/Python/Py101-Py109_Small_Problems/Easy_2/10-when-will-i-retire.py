'''
Build a program that displays when the user will retire and how many years she has to work till retirement.
'''

'''
    What is your age? 30
    At what age would you like to retire? 70

    It's 2024. You will retire in 2064.
    You have only 40 years of work to go!
'''

from datetime import date

age = int(input('what is your age?: '))
retire_age = int(input('at what age would you like to retire?: '))
years_to_go = retire_age - age
current_year = date.today().year

print(f'The yaer is {current_year}.  You will retire in {current_year + years_to_go}')
print(f'You only have {years_to_go} years of work to go!')
