# rescue_practice.rb

def divide_by_zero(num, divisor)
  begin
    answer = num / divisor
  rescue ZeroDivisionError => e
    puts e.message
  end
end

divide_by_zero(10,0)

def make_the_call()
  zero = 0
  puts "Before the call"
  zero.each {|a| puts a} rescue puts "Error reached"
  puts "after the call"
end

make_the_call()
