# frozen_string_literal: true

# Build a program that asks a user for the length and width of a room in meters
# and then displays the area of the room in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# Do not worry about validating the input at this time.

SQ_METER_TO_SQ_FEET = 10.7639

def room_area
  puts 'Enter the length of the room in meters:'
  length = gets.chomp.to_i
  puts 'Enter the wideth of the room in meters:'
  width = gets.chomp.to_i
  sq_m = (length * width).to_f
  sq_ft = sq_m * SQ_METER_TO_SQ_FEET
  puts "The area of the room is #{sq_m} square meters (#{sq_ft} square feet)."
end

room_area
