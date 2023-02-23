def substrings(str)
  str_substring = []
  counter = 0
  loop do
    str_substring << str[0..counter]
    counter += 1
    break if counter == str.size
  end
  str_substring
end

p substrings('abc')
