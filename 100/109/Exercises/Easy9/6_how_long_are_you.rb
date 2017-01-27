def word_len(str)
  str.split.map {|word| "#{word} #{word.size}"}
end

p word_len("cow sheep chicken")
