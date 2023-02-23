def word_counter(str)
  container = Hash.new(0)
  str.split.each do |word|
    container[word.size] += 1
  end
  container
end

def word_count_only_letters(str)
  str = str.split
  str.map do |el|
    # el.delete!('^a-z','^A-Z')
    el.gsub!(/[^a-z]/i, '')
  end

  word_counter(str.join(' '))
end

p word_count_only_letters("")
