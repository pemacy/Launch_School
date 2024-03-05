'''
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime class methods.
'''

MINUTES_IN_A_DAY = 1_440

def get_hours_mins(time):
    return [ int(el) for el in time.split(':') ]

def after_midnight(time):
    if time == '24:00': time = '00:00'

    hours, mins = get_hours_mins(time)
    mins =  hours * 60 + mins
    return mins

def before_midnight(time):
    if time == '00:00': time = '24:00'

    hours, mins = get_hours_mins(time)
    mins = MINUTES_IN_A_DAY - hours * 60 - mins
    return mins

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
