# frozen_string_literal: true

# Write a method that will take a short line of text, and print it within a box.

def print_in_box(str)
  dash_inserts = '-' * str.length
  horiz_border = '+-' + dash_inserts + '-+'
  space_inserts = ' ' * str.length
  padding_border = '| ' + space_inserts + ' |'
  puts horiz_border
  puts padding_border
  puts '| ' + str + ' |'
  puts padding_border
  puts horiz_border
end

print_in_box('To boldly go where no one has gone before.')

print_in_box('')
