# frozen_string_literal: false

# Write a method that takes a String as an argument, and returns a new String
# that contains the original value using a staggered capitalization scheme in
# which every other character is capitalized, and the remaining characters are
# lowercase. Characters that are not letters should not be changed, but count
# as characters when switching between upper and lowercase.

def staggered_case(str)
  str.chars.each_with_index.with_object('') do |(c, i), str_2|
    str_2 << c.upcase if i.even?
    str_2 << c.downcase if i.odd?
  end
end

puts staggered_case('I Love Launch School!') == 'I LoVe lAuNcH ScHoOl!'
puts staggered_case('ALL_CAPS') == 'AlL_CaPs'
puts staggered_case('ignore 77 the 444 numbers') == 'IgNoRe 77 ThE 444 NuMbErS'
