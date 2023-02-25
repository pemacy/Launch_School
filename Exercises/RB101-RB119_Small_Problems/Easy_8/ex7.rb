# frozen_string_literal: false

# Write a method that takes a string, and returns a new string in which every
# consonant character is doubled. Vowels (a,e,i,o,u), digits, punctuation, and
# whitespace should not be doubled.

def double_consonants(str)
  str.chars.each_with_object('') do |c, double_str|
    if c =~ /[^(aeiouAEIOU)|\W|\d]/
      double_str << c * 2
    else
      double_str << c
    end
  end
end

p double_consonants('String') == "SSttrrinngg"
p double_consonants("Hello-World!") == "HHellllo-WWorrlldd!"
p double_consonants("July 4th") == "JJullyy 4tthh"
p double_consonants('') == ""
