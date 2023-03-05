# frozen_string_literal: true

# Write a method that takes one argument, a string containing one or more words,
# and returns the given string with words that contain five or more characters
# reversed. Each string will consist of only letters and spaces. Spaces should
# be included only when more than one word is present.

def reverse_words(str)
  str.split.map do |word|
    if word.size > 4
      word.chars.reverse.join
    else
      word
    end
  end.join(' ').strip
end

puts reverse_words('Professional') == "lanoisseforP"          # => lanoisseforP
puts reverse_words('Walk around the block') == "Walk dnuora the kcolb" # => Walk dnuora the kcolb
puts reverse_words('Launch School') == "hcnuaL loohcS"         # => hcnuaL loohcS
