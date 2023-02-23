input = nil

loop do
  loop do
    puts "How many output lines do you want? Enter a number >= 3 (Q to quit)"
    input = gets.chomp
    break if input.to_i >= 3 || input.downcase.eql?('q')
    puts "Your number was not greater or equal to 3"
  end
  break if input.downcase.eql?('q')
  while input.to_i > 0
    puts "Launch School is the best!"
    input.to_i -= 1
  end

end

puts "Goodbye!"
