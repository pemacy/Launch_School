# frozen_string_literal: true

# The following code throws an error. Find out what is wrong and think about how
# you would fix it.

colors = ['red', 'yellow', 'purple', 'green', 'dark blue', 'turquoise', 'silver', 'black']
things = ['pen', 'mouse pad', 'coffee mug', 'sofa', 'surf board', 'training mat', 'notebook']

colors.shuffle!
things.shuffle!

i = 0
loop do
  break if i > colors.length

  if i == 0
    puts 'I have a ' + colors[i] + ' ' + things[i] + '.'
  else
    puts 'And a ' + colors[i] + ' ' + things[i] + '.'
  end

  i += 1
end

# => 2 issues:
# 1. colors.length is 1-indexed, where elelment indexing of an array is 0-indexed,
# so once i gets to colors.length, it will be more than the amount of elements in
# colors array, but will go through the loop once more, so it should end at
# i > colors.length - 1
# 2. there are more items in colors array than in things array, so when it gets to
# i = 7, there is no index 7 element for the things array
# to solve this you can use things.length -1 as the limit of the loop
