'''
A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?
'''

'''
Use a sorting function like sorted(list(set(data))) or mutate the list through list(set(data)).sort()
'''

data = [1, 2, 3, 2, 4, 3]
unique_data = sorted(list(set(data)))
print(unique_data)  # The order is not guaranteed to be [1, 2, 3, 4]
