# 2_text_analyzer.rb

class TextAnalyzer
  def process
    @file = File.open("pg85.txt")
    yield(@file.read)
    @file.close
  end

  def count_lines
    @text.size
  end

  def count_words
    @text.split.size
  end

  def count_paragraphs
    @text.split("\n").size
  end
end

analyzer = TextAnalyzer.new
analyzer.process { |file| puts "#{file.split("\n\n").size} paragraphs" }
analyzer.process { |file| puts "#{file.split("\n").size} lines" }
analyzer.process { |file| puts "#{file.split.size} words" }
