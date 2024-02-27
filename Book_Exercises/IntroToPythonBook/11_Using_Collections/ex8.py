text = "It's probably pining for the fjords!"

print(text[21:31])
print(text[21:31].rfind('f'))
print(text.rfind('f', 21, 35))

# The difference between the two is:
# The first rfind finds the highest index of f in the substring of 'It's probably pining for the fjords!', which is 'for the fj'
# The second finds the highest index of x between the indexes of 21 and 35 of the original text string
