def fizzbuzz(start, last)
  fizbuz = []
  start.upto(last) do |n|
    if n % 3 == 0 && n % 5 == 0
      fizbuz << 'FizzBuzz'
    elsif n % 3 == 0
      fizbuz << 'Fizz'
    elsif n % 5 == 0
      fizbuz << 'Buzz'
    else
      fizbuz << n
    end
  end
  fizbuz
end

p fizzbuzz(1, 15)
