# frozen_string_literal: true

require 'date'

puts Date.civil
puts Date.civil(2016)
puts Date.civil(2016, 5)
puts Date.civil(2016, 5, 13)

# What will each of the 4 puts statements print?

# 1. Returns a date object with year -4712 (BC) Jan 1
# 2. Returns a date object with the year 2016, Jan 1
# 3. Returns a date object with year 2016, month 5, day 1
# 4. Returns a date object with eyar 2016, month 5, day 13
