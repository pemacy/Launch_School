class Palindromes
  def initialize(max_factor: nil, min_factor: 1)
    @max = max_factor
    @min = min_factor
  end

  def generate
    @palendrome_products = Hash.new([])

    @min.upto(@max) do |n1|
      for n2 in (n1.. @max)
        result = n1 * n2
        # p [result.to_s, result.to_s.reverse]
        if result.to_s == result.to_s.reverse
          @palendrome_products[result] += [[n1,n2]]
        end
      end
    end
  end

  def largest
    AnalyzePalindrome.new(@palendrome_products.max)
  end

  def smallest
    AnalyzePalindrome.new(@palendrome_products.min)
  end

  class AnalyzePalindrome
    def initialize(palindro)
      @palindro = palindro
    end

    def value
      @palindro.first
    end

    def factors
      @palindro.last
    end
  end
end

palindromes = Palindromes.new(max_factor: 9)
palindromes.generate
p palindromes.largest.factors
p palindromes.largest.value
