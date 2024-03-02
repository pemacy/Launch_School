'''
Madlibs is a simple game where you create a story template with "blanks" for words. You, or another player, then construct a list of words and place them into the story, creating an often silly or funny story as a result.

Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you create.
'''

verb = input('Enter a verb: ')
noun = input('Enter a noun: ')
adj = input('Enter an adjective: ')
adv = input('Enter an adverb: ')

print(f'The {adj} {noun} {verb} {adv} over the lazy dog')
