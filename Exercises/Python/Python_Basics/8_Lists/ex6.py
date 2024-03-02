'''
You've been given a list of vocabulary words grouped into sub-lists, by meaning. This is a two-dimensional list or a nested list. Write some code that iterates through and prints all the words, one per line.
'''

def print_els(lst):
    for el in lst:
        if isinstance(el, list):
            print_els(el)
        else:
            print(el)

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

print_els(vocabulary)

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...
