'''
Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).
'''

def clean_up(s):
    result = ''.join([ ' ' if not l.isalpha() else l for l in s ])
    new_str = ''
    last_letter = ''
    for l in result:
        if last_letter.isspace() and l.isspace():
            next
        else:
            new_str +=l
        last_letter = l

    print(new_str)
    return new_str

print(clean_up("---what's my +*& line?") == " what s my line ")
# True
