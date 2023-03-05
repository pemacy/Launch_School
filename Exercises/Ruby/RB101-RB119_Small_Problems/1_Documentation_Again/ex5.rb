# frozen_string_literal: true

# What do each of these puts statements output?

a = %w(a b c d e)
# puts a.fetch(7)
puts a.fetch(7, 'beats me')
puts a.fetch(7) { |index| index**2 }

# 1. returns an IndexError because there is no element at index 7
# 2. prints 'beats me', because there is no el at idx 7, but it has a default value
# 3. prints 49, because the default is index value squared
