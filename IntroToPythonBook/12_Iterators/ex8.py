my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

new_dict = { el: len(el) for el in my_set if len(el) % 2 != 0 }
print(new_dict)
