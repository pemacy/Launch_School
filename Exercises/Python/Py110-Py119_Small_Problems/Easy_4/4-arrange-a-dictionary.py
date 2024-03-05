'''
Given a dictionary, return its keys in an ordered list based on the associated values.
'''

def order_by_value(d):
    return sorted(d.keys())

print(order_by_value({'p': 8, 'q': 2, 'r': 6}))
# ['q', 'r', 'p']
