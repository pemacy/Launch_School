class Prime
  def self.nth(num)
    raise ArgumentError if num.zero?

    primes, chk = [2], 3

    until primes.size == num do
      primes << chk unless (2..Math.sqrt(chk)).any? {|n| (chk % n).zero? }
      chk += 1
    end

    primes.last
  end
end

p Prime.nth(20)
