'''
Is there a method to reverse a string, for example turning 'hello' into 'olleh'?
'''

dir(str)

'''
[
    '__add__',          '__class__',            '__contains__', '__delattr__',      '__dir__',
    '__doc__',          '__eq__',               '__format__',   '__ge__',           '__getattribute__',
    '__getitem__',      '__getnewargs__',       '__getstate__', '__gt__',           '__hash__',
    '__init__',         '__init_subclass__',    '__iter__',     '__le__',           '__len__',
    '__lt__',           '__mod__',              '__mul__',      '__ne__',           '__new__',
    '__reduce__',       '__reduce_ex__',        '__repr__',     '__rmod__',         '__rmul__',
    '__setattr__',      '__sizeof__',           '__str__',      '__subclasshook__', 'capitalize',
    'casefold',         'center',               'count',        'encode',           'endswith',
    'expandtabs',       'find',                 'format',       'format_map',       'index',
    'isalnum',          'isalpha',              'isascii',      'isdecimal',        'isdigit',
    'isidentifier',     'islower',              'isnumeric',    'isprintable',      'isspace',
    'istitle',          'isupper',              'join',         'ljust',            'lower',
    'lstrip',           'maketrans',            'partition',    'removeprefix',     'removesuffix',
    'replace',          'rfind',                'rindex',       'rjust',            'rpartition',
    'rsplit',           'rstrip',               'split',        'splitlines',       'startswith',
    'strip',            'swapcase',             'title',        'translate',        'upper',
    'zfill'
]
'''

'''
No, there is no method to reverse a string, but you could convert it to a list, reverse the list, and convert it back to a string
'''

s = 'hello'
s = list(s)
s.reverse()
s = ''.join(s)

'''
Alternate using slicing

s = 'hello'
print(s[::-1])

slice notation: [start:stop:step]
- if step is negative it is [stop:start:-step]

ex:
    s = 'abcdef'
    s[0:3:1] = 'abcd'
    s[0:2:1] = 'abc'
    s[0:3:2] = 'ac' --> s[0] = 'a', s[0 + 2] = h[2] = 'c'
    s[3:0:-1] = 'dcba' --> s[3] = 'd', s[2] = 'c', s[1] = 'b', s[0] = 'a'
    s[3:0:-2] = 'db'

    s[::] = s[0:last_index:1]
    s[::-1] = s[last_index:0:-1]
'''
