'''
Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line indented 1 space to the right of the line above it. The output should start out like this:
'''

line = "The Flintstones Rock!"

for i in range(10):
    spacing = i * ' '
    print(spacing, line)
