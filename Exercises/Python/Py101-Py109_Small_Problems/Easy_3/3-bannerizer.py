'''
Write a function that takes a short line of text and prints it within a box.
'''

def print_in_box(s):
    s_len = len(s)
    vert_border = '+-' + '-' * s_len + '-+'
    mid_line = '| ' + ' ' * s_len + ' |'

    print(vert_border)
    print(mid_line)
    print(f'| {s} |')
    print(mid_line)
    print(vert_border)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')
