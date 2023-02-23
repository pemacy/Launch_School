# frozen_string_literal: true

# In an earlier exercise, you wrote a program that prints
# 'Launch School is the best!' repeatedly until a certain number
# of lines have been printed. Our solution looked like this:

number_of_lines = nil

def lsprint(number_of_lines)
  while number_of_lines.positive?
    puts 'Launch School is the best!'
    number_of_lines -= 1
  end
end

loop do
  puts '>> How many output lines do you want? Enter a number >= 3: (Q to quit)'
  number_of_lines = gets
  break if number_of_lines =~ /q/i

  number_of_lines = numbers_of_lines.to_i
  lsprint(number_of_lines) if number_of_lines >= 3
  puts ">> That's not enough lines." if number_of_lines < 3
end
