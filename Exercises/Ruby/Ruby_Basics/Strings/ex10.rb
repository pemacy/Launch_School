# frozen_string_literal: true

# Using the following code, print true if colors includes the color 'yellow'
# and print false if it doesn't. Then, print true if colors includes the color
# 'purple' and print false if it doesn't.

colors = 'blue pink yellow orange'

puts colors.split.include?('yellow')
puts colors.split.include?('purple')
