'''
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.
'''

def word_sizes(s):
    sizes = {}
    for word in s.split():
        if len(word) in sizes:
            sizes[len(word)] += 1
        else:
            sizes[len(word)] = 1
    return sizes

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
