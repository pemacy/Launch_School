# countdown.rb

x = gets.chomp.to_i

while x >= 0
  puts x
  x -= 1
end

puts"done!"

# countdown.rb using until loop

x = gets.chomp.to_i

until x < 0
  puts x
  x -= 1
end

puts "Done again with the until loop"
