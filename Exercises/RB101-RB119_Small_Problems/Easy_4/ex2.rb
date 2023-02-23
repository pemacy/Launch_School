# frozen_string_literal: true

# Write a method that takes a year as input and returns the century. The return
# value should be a string that begins with the century number, and ends with
# st, nd, rd, or th as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901-2000
# comprise the 20th century.

# 1. find century digits
# 2. find year digits
# 3. perform logic

def century(year)
  return '1st' if (year / 100).zero?

  century_digits = first_digits(year)
  cent = if (year % 100).positive?
           1
         else
           0
         end
  cent += century_digits.to_i
  cent.to_s + suffix(cent.to_s)
end

def first_digits(num)
  num = num.to_s.chars
  num.pop(2)
  num.join
end

def suffix(num)
  num = num[-2, 2] if num.size > 2
  if num.to_i > 3 && num.to_i < 21
    'th'
  elsif num.chars.last == '1'
    'st'
  elsif num.chars.last == '2'
    'nd'
  elsif num.chars.last == '3'
    'rd'
  else
    'th'
  end
end

puts century(2000) == '20th'
puts century(2001) == '21st'
puts century(1965) == '20th'
puts century(256) == '3rd'
puts century(5) == '1st'
puts century(10_103) == '102nd'
puts century(1052) == '11th'
puts century(1127) == '12th'
puts century(11_201) == '113th'
