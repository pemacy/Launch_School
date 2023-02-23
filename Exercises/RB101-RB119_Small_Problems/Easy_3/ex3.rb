# frozen_string_literal: true

def num_char
  puts 'Please write word or multiple words:'
  words = gets.chomp
  count = words.split.join('').size
  puts "Thre are #{count} characters in \"#{words}\""
end

num_char
