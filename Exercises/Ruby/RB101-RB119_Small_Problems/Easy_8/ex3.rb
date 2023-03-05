#  frozen_string_literal: true

def substrings(str)
  str.chars.each_with_index.with_object([]) do |(_c, i), arr|
    str.chars[i..-1].each_with_index do |_chr, idx|
      arr << str.chars[i..-1][0..idx].join
    end
  end
end

p substrings('abcde') == [
  'a', 'ab', 'abc', 'abcd', 'abcde',
  'b', 'bc', 'bcd', 'bcde',
  'c', 'cd', 'cde',
  'd', 'de',
  'e'
]
