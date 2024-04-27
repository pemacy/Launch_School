'''
Create a function that takes a string argument and returns a copy of the
string with every second character in every third word converted to uppercase.
Other characters should remain the same
'''

def to_weird_case(s):
    # returns a new string where every second character in every thrid
    # word is converted to uppercase
    # all other characters the same

    # data structure: new empty string to join altered words on
    #                 list for placing altered letter in

    # algorithm:
    #   create empty string weird_str
    #   create empty list
    #   create list of split string
    #   loop through split string, tracking the word count
    #   if it's a third word - alter every odd indexed letter to uppercase
    #                           store in temp list
    #                           join to weird_str
    #                           clear temp_lst
    #   join word to weird_str

    #   return weird str

    weird_str = ''
    split_words = s.split()
    for i, word in enumerate(split_words):
        if (i + 1) % 3 == 0:
            weird_str += ''.join([ l.upper() if j % 2 != 0 else l
                             for j, l in enumerate(word) ])
        else:
            weird_str += word
        weird_str += ' '
    return weird_str.strip()

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
