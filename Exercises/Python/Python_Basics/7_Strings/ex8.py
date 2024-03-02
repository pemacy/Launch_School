'''
Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.
'''

s = 'launch school tech & talk'
print(s.title())

s1 = ' '.join([w.capitalize() for w in s.split()])
print(s1)
