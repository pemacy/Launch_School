'''
The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime class methods.
'''

MINUTES_IN_A_DAY = 1_440

def time_of_day(mins):
    # mins corrected for overflow minutes
    mins = mins % MINUTES_IN_A_DAY

    hours, mins = divmod(mins, 60)

    # hours and mins formatted appropriately
    hours = str(hours).rjust(2, "0")
    mins = str(mins).rjust(2, "0")

    time = f'{hours}:{mins}'
    return time

    # mins to hours

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
