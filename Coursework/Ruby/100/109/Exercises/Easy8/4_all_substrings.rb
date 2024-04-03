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

def all_substrings(str)
  all_sub = []
  0.upto(str.size - 1) do |index|
    all_sub += substrings(str[index..-1])
  end
  all_sub
end

p all_substrings('abc')
