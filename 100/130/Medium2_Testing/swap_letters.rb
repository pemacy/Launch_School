class Text
  attr_accessor :text

  def initialize(text)
    @text = text
  end

  def swap(letter_one, letter_two)
    @text.gsub(letter_one, letter_two)
  end

  def word_count
    @text.split.count
  end
end

file = File.open("./loren.txt", "r")
txt = Text.new(file.read)
p txt.word_count
