def word_counter(str)
  container = Hash.new(0)
  str.split.each do |word|
    container[word.size] += 1
  end
  container
end

p word_counter('Four score and seven')
