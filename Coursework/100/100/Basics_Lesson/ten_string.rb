# ten_string.rb

p "Enter a string:"
str = gets.chomp

if str.length > 10
  p str.upcase
else
  p str.downcase
end
