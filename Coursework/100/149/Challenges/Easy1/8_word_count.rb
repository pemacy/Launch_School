class Phrase
  attr_accessor :words
  def initialize(phrase)
    phrase.gsub!(/'(\w+)'/,'\1')
    @words = phrase.split(/[^\w+'?]/).select{ |w| w =~ /\w+'?/ }
  end

  def word_count
    @words.each_with_object(Hash.new(0)) { |w,h| h[w.downcase] += 1}
  end
end


# phrase = phrase = Phrase.new("Joe can't tell between 'large' and large.")
# p phrase.words
#
# phrase = phrase = Phrase.new("one,\ntwo,\nthree")
# p phrase.words
#
# phrase = phrase = Phrase.new('one,two,three')
# p phrase.words
