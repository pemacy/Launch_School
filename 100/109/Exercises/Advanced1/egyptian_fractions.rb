# egyptian_fractions.rb

def egyptian(num)
  arr, counter = [], 1
  loop do
    sum = (arr + [counter]).reduce(0) { |sum, n| sum += Rational(1, n) }
    arr << counter if sum <= num
    sum == num ? break : counter += 1
  end
  arr
end

def unegyptian(arr)
  arr.reduce(0) { |sum, n| sum += Rational(1,n) }
end

def egypt2(num)
  (1..Float::INFINITY).each_with_object([]) do |denom, arr|
    sum = (arr + [denom]).reduce(0) { |sum, n| sum += Rational(1, n) }
    arr << denom if sum <= num
    return arr if sum == num
  end
end

p egypt2(Rational(137,60))
p egyptian(Rational(2,1))
p egyptian(Rational(137, 60))
p egyptian(Rational(3,1))
p unegyptian(egypt2(Rational(3,1)))
