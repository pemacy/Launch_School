# frozen_string_literal: true

# Write a method that takes a sentence string as input, and returns the same
# string with any sequence of the words 'zero', 'one', 'two', 'three', 'four',
# 'five', 'six', 'seven', 'eight', 'nine' converted to a string of digits.

NUMBER_WORDS = %w[zero one two three four five six seven eight nine].freeze
NUMBER_REGEX = /(one|two|three|four|five|six|seven|eight|nine|zero)(.*)/.freeze

def word_to_digit(str)
  str.split.map do |word|
    if word.match(NUMBER_REGEX)
      word.gsub(NUMBER_REGEX) { NUMBER_WORDS.index($1).to_s + $2 }
    else
      word
    end
  end.join(' ')
end

p word_to_digit('Please call me at five five five one two three four. Thanks.') == 'Please call me at 5 5 5 1 2 3 4. Thanks.'
