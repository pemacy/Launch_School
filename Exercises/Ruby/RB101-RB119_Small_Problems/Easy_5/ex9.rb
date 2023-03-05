# frozen_string_literal: false

# Write a method that takes a string argument and returns a new string that
# contains the value of the original string with all consecutive duplicate
# characters collapsed into a single character. You may not use String#squeeze
# or String#squeeze!.

def crunch(str)
  str.split.each_with_object([]) do |word, arr|
    arr << word.chars.each_with_object('') do |c, s_2|
      s_2 << c if s_2.chars.last != c
    end
  end.join(' ')
end

puts crunch('ddaaiillyy ddoouubbllee') == 'daily double'
puts crunch('4444abcabccba') == '4abcabcba'
puts crunch('ggggggggggggggg') == 'g'
puts crunch('a') == 'a'
puts crunch('') == ''
