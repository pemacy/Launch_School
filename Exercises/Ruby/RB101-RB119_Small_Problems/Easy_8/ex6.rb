# frozen_string_literal: false

# Write a method that takes a string, and returns a new string in which every
# character is doubled.

def repeater(str)
  str.chars.each_with_object('') do |c, double_str|
    double_str << c * 2
  end
end

p repeater('Hello') == "HHeelllloo"
p repeater("Good job!") == "GGoooodd  jjoobb!!"
p repeater('') == ''
