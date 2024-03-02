'''
We have a grocery list. As we check off items on that list, we want to remove them from the list.

Write code that removes the items from grocery_list, one by one, until it is empty. If you print the elements you remove, the expected behavior would look as follows.
'''

def remove_all_items(lst):
    while lst:
        print(lst.pop(0))

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.

remove_all_items(grocery_list)

print(grocery_list)
