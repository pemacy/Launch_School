require 'pry'

module OddWords
  def self.odderize(str)
    raise ArgumentError, validate(str) if validate(str)
    reverse_odds(str[0..-2]).join(' ') + str[-1]
  end


  def self.odderize_bonus(str)
  end

  private

  def self.reverse_odds(str)
    string = str.split.each_with_index.inject [] do |string, (word, idx)|
      punc = ''
      word, punc = word[0..-2], word[-1] if word[-1] =~ /\W/
      string << (idx.even? ? word : word.reverse + punc)
    end
  end

  def self.validate(str)
    return "Wrong data type" if str.class != String
    return "No input given" if str.empty?
    return "Doesn't end in a period" if str[-1] != '.'
    for word in str.split
      return "There is a word greater than 20 chars" if word.size > 20
      return "Invalid word >#{word}<" unless word =~ /^\w+/ || word == '.'
    end
    false
  end
end

p OddWords.odderize('One fish tw?o fish, red fish blue fish .')
