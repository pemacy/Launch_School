from datetime import datetime
# from datetime import time

'''
Using the datetime module in Python, how would you obtain the current date and time?
'''

now = datetime.now()
print(now.strftime('Date is: %d %b, %y, and the Time is: %I:%M'))
