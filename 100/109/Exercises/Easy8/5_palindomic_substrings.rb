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

def palindromes(str)
  palindromes_possibilities = all_substrings(str)
  palindro = []
  palindromes_possibilities.each do |sub_str|
    palin << sub_str if sub_str == sub_str.reverse && sub_str.size > 1
  end
  palindro
end

p palindromes('hello-madam-did-madam-goodbye')
