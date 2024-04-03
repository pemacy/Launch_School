puts "Teddy is #{rand(20..100)} years old"

puts "Enter name of a person"
name = gets.chomp

puts "#{name.empty? ? 'Teddy' : name} is #{rand(20..100)} years old"
