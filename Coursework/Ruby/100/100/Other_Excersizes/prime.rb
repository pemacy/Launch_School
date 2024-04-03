# prime.rb

def is_prime(num)
  for i in 2..num-1
    if num % i == 0
      return false
    end
  end
  return true
end

def find_primes(num)
  primes = []
  for i in 2..num
    test_prime = true
    for j in 2..i-1
      if i % j == 0 then
        test_prime = false
        break
      end
    end
    if test_prime == true then primes.push(i) end
  end
  primes
end

loop do
  puts "Here are your choices:"
  puts "========================================="
  puts "1. Enter a number to see if it's prime"
  puts "2. Find the first 'x' number of primes up to a number you enter"
  puts "3. Quit by typing 'q' and pressing enter"
  puts "========================================="
  input = gets.chomp
  if input == 'q' then break end
  case input.to_i
  when 1
    system("clear")
    print "Enter a number: "
    num = gets.chomp.to_i
    puts is_prime(num)
  when 2
    system("clear")
    print "Enter a number to see how many primes are in it: "
    num = gets.chomp.to_i
    num_primes = find_primes(num)
    puts "There are #{num_primes.length} prime numbers, they are:"
    print num_primes.to_s + "\n\n"
  end
end
