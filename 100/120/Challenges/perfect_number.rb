class NumberTester
  attr_accessor :number

  def initialize(n)
    self.number = n
  end

  def number_type
    puts "Number is #{number}, Divisors are #{divisors}, Divisor Sum is #{divisors.reduce(:+)}"
    return 'perfect' if divisors.reduce(:+) == number
    return 'deficient' if divisors.reduce(:+) < number
    'abundant'
  end

  private

  def divisors
    storage = []
    1.upto(number / 2) do |n|
      storage << n if number % n == 0
    end
    storage
  end
end

num = NumberTester.new(12)
p num.number_type
