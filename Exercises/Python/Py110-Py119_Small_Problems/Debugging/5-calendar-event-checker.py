'''
We have a list of events, and we want to check if a specific date is available (i.e., no events planned for that day). However, the function always seems to think the date is available, even when it's not.
'''

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"]
}

'''
The logic is backwards, if date is in events that means the date is NOT available and should return False, otherwise True
'''

def is_date_available(date):
    if date in events:
        return True
    return False

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True
