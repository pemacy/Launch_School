module PerfectNumber
  def self.initialize
    puts "Hey y'all!"
  end

  def self.classify(num)
    @@num = num
    validate
    multiples = get_multiples
    determine_number(multiples)
  end

  private

  def self.validate
    raise RuntimeError if @@num < 1
  end

  def self.get_multiples
    (1..@@num-1).to_a.select{|n| @@num % n == 0}
  end

  def self.determine_number(m)
    case m.reduce(&:+) <=> @@num
    when 1 then 'abundant'
    when 0 then 'perfect'
    when -1 then 'deficient'
    end
  end
end


# p PerfectNumber.classify(-1)
