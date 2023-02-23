def balanced?(str)
  counter = 0
  str.chars.each do |c|
    counter += 1 if c == '('
    counter -= 1 if c == ')'
    return false if counter < 0
  end
  counter.zero?
end

puts balanced?('()?')
