def word_cap(str)
  str.split.map {&:capitalize}.join(' ')
end

p word_cap('four score and seven')
