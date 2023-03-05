# frozen_string_literal: true

# Write a program that solicits 6 numbers from the user, then prints a message
# that describes whether or not the 6th number appears amongst the first
# 5 numbers.

def solicit_5
  arr = []
  num_endings = ['1st', '2nd', '3rd', '4th', '5th', 'last']
  6.times do |n|
    puts "Enter the #{num_endings[n]} number:"
    arr << gets.chomp.to_i
  end
  last = arr.pop
  if arr.include?(last)
    puts "The number #{last} does appear in #{arr}"
  else
    puts "The number #{last} does not appear in #{arr}"
  end
end

solicit_5
