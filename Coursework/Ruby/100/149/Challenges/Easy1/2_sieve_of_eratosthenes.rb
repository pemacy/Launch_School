class Sieve
  def initialize(num)
    @num = num
    @primes = (2..@num).to_a
  end

  def primes
    2.upto(@num * 0.5) do |n|
      2.upto(@num ** 0.5) do |n2|
        @primes.delete(n * n2)
      end
    end
    @primes
  end
end

primes = Sieve.new(10)
p primes.primes
