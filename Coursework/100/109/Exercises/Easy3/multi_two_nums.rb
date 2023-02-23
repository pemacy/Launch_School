def multiply(first_num, second_num)
  first_num.send(:*, second_num)
end

puts multiply(5, 3) == 15
