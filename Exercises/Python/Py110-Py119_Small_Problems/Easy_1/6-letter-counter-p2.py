'''
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.
'''

def word_sizes(s):
    size_dict = {}
    for w in s.split():
        w = ''.join([ l if l.isalpha() else '' for l in w ])
        w_len = len(w)

        if w_len in size_dict:
            size_dict[w_len] += 1
        else:
            size_dict[w_len] = 1
    return size_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
