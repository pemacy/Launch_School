# frozen_string_literal: true

# Print all odd numbers from 1 to 99, inclusive, to the console, with each
# number on a separate line.

puts (1..99).select(&:odd?)
