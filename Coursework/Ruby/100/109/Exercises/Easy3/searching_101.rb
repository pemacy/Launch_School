require 'ordinalize'

def input(num)
  arr = []
  num.times do |n|
    if n == num - 1
      puts "Enter the last number"
      arr[n] = gets.chomp.to_i
    else
      puts "Enter the #{(n+1).ordinalize} number"
      arr[n] = gets.chomp.to_i
    end
  end
  arr
end

def is_present?(arr)
  if arr[0..arr.size-2].include?(arr.last)
    puts "The number #{arr.last} appears in #{arr[0..arr.size-2].to_s}"
  else
    puts "The number #{arr.last} does not appear in #{arr[0..arr.size-2].to_s}"
  end
end

puts "How many numbers would you like to input?:"
num = gets.chomp.to_i
is_present?(input(num))
