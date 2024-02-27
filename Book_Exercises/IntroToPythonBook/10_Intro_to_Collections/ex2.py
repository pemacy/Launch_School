stuff = ('hello', 'world', 'bye', 'now')

# change bye to goodbye

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)
