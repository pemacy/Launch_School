# frozen_string_literal: true

def leading_substrings(str)
  str.chars.each_with_index.with_object([]) do |(c, i), arr|
    arr << str.chars[0..i].join
  end
end

p leading_substrings('abc') == ['a', 'ab', 'abc']
p leading_substrings('a') == ['a']
p leading_substrings('xyzzy') == ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']
