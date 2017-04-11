class Scrabble
  SCORES = {1 => %w(A E I O U L N R S T), 2 => %w(D G), 3 => %w(B C M P),
            4 => %w(F H V W Y), 5 => %w(K), 8 => %w(J X), 10 => %w(Q Z)}

  def initialize(word)
    @word = word
  end

  def self.score(word)
    return 0 if word.class != String || word =~ /\W|\d/ || word.empty?
    word.chars.each.inject 0 do |sum, letter|
      SCORES.each { |k,v| sum += k if v.include?(letter.upcase) }
      sum
    end
  end

  def score
    self.class.score(@word)
  end
end

# p Scrabble.new('aaa').score
