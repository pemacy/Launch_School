# frozen_string_literal: true

#

def tip_calc
  puts 'What is the bill?'
  bill = gets.chomp.to_i
  puts 'What is the tip percentage'
  tip_percent = gets.chomp.to_f
  tip = (tip_percent / 100.0) * bill
  puts "The tip is $#{tip}"
  puts "The bill is $#{bill.to_f}"
end

tip_calc
