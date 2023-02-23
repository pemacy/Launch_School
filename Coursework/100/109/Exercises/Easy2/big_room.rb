def area_of_room(length, width)
  area = length * width
  [area, area*10.7369]
end

puts "Enter the legnth of the room in meters:"
length = gets.chomp
puts "Enter the width of the room in meters:"
width = gets.chomp

area = area_of_room(length.to_f, width.to_f)
puts "The area of the room is #{area[0]} square meters (#{area[1]} square feet)."
