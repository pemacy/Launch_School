print 'Enter a number: '
num = gets.to_i
puts 'Enter the digit of the number you\'d like to find (1=1\'s, 2=10\'s, 3=100\'s, etc)'
dig = gets.to_i
num_len = num.to_s.length.to_i
puts "num length = #{num_len}"

while (num_len - dig) != 0
  puts "num = #{num}"
  puts "num length = #{num_len}"
  num = num % (10**(num_len -1))  #Reduce num by the left most digit
  puts "num = #{num}"
  num_len = num.to_s.length.to_i    #Decriments num_len by one
  puts "num_len = #{num_len}"
end
num = num / (10**(num_len - 1))
print num
