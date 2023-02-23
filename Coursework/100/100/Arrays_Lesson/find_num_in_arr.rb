# find_num_in_arr.rb

arr = [1, 3, 5, 7, 9, 11]

p 'Enter number to search for in array: '
number = gets.chomp.to_i

if arr.include?(number)
  p "#{number} is in the array"
else
    p "#{number} is not in the array"
end
