# case_statement.rb

a = 5

case a
when 5
  p 'a is 5'
when 6
  p 'a is 6'
else
  p 'a is neither 5, nor 6'
end


# case_statement.rb < -- refactored

answer = case a
when 5
  'a is 5'
when 6
  'a is 6'
else
  'a is neither 5, nor 6'
end

puts answer

# case_statement.rb < -- refactored with no case argument

answer = case
when a == 5
  'a is 5'
when a == 6
  'a is 6'
else
  'a is neither 5, nor 6'
end

puts answer
