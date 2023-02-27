# frozen_string_literal: true

# Write a method that takes a string as an argument, and returns true if all
# parentheses in the string are properly balanced, false otherwise. To be
# properly balanced, parentheses must occur in matching '(' and ')' pairs.

def balanced?(str)
  count = 0
  str.chars.each do |chr|
    count += 1 if chr == '('
    count -= 1 if chr == ')'
    break if count.negative?
  end
  count.zero?
end

p balanced?('What (is) this?') == true
p balanced?('What is) this?') == false
p balanced?('What (is this?') == false
p balanced?('((What) (is this))?') == true
p balanced?('((What)) (is this))?') == false
p balanced?('Hey!') == true
p balanced?(')Hey!(') == false
p balanced?('What ((is))) up(') == false
