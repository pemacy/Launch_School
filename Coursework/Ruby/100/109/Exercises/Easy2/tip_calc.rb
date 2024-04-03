def get_tip(bill, tip_rate)
  bill.to_f * tip_rate.to_f / 100
end

print "What is the bill?  "
bill = gets.chomp
print "What is the tip percentage?  "
tip_rate = gets.chomp
tip = get_tip(bill, tip_rate).round(2)
total = bill.to_f + tip
puts "\nThe tip is $#{format("%0.2f",tip)}"
puts "The total is $#{format("%0.2f",total)}"
