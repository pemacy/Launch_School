# frozen_string_literal: true

# Write a method that takes a positive integer as an argument and returns that
# number with its digits reversed. Examples:

def reversed_number(num)
  num.to_s.split('').reverse.join('').to_i
end

puts reversed_number(12345) == 54321
puts reversed_number(12213) == 31221
puts reversed_number(456) == 654
puts reversed_number(12000) == 21 # No leading zeros in return value!
puts reversed_number(12003) == 30021
puts reversed_number(1) == 1
