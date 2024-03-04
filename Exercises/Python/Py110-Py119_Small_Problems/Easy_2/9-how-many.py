'''
Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
'''

def count_occurrences(lst):
    h = {}
    for el in lst:
        if el in h:
            h[el] += 1
        else:
            h[el] = 1
    for key, value in h.items():
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

'''
# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2
'''
