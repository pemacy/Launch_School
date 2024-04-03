s = nil
loop do
  puts "Do you want to print something?"
  s = gets.chomp.downcase
  break if ['n','y'].include?(s)
    puts "invalid input"
end
puts "something" if s == 'y'
