# frozen_string_literal: true

# Given a string of words separated by spaces, write a method that takes this
# string of words and returns a string in which the first and last letters of
# every word are swapped.

# You may assume that every word contains at least one letter, and that the
# string will always contain at least one word. You may also assume that each
# string contains nothing but words and spaces/

def swap(str)
  str.split.map do |word|
    word = word.chars
    if word.size == 1
      word
    else
      first = word.shift
      last = word.pop
      last + word.join('') + first
    end
  end.join(' ')
end

puts swap('Oh what a wonderful day it is') == 'hO thaw a londerfuw yad ti si'
puts swap('Abcde') == 'ebcdA'
puts swap('a') == 'a'
