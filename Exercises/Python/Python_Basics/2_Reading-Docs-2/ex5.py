'''
The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.
'''

from datetime import date

today = date.today()

print(type(date))
print(type(today))

today_year = today.year
iso_year = today.isocalendar()[0]

print(today_year)
print(iso_year)

'''
What is the difference between the year attribute and the isocalendar method?
isocalendar - the week starts Monday and ends Sunday
            - consists of 52 or 53 weeks
            - first week of the year is calendar week containing a Thursday

'''
