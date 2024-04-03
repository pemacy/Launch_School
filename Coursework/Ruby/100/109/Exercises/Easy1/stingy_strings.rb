def stringy(int, opt = 0)
  string = ''
  if opt == 0
    int.times { |n| n.even? ? string << '1' : string << '0'}
  else
    int.times { |n| n.odd? ? string << '1' : string << '0'}
  end
  string
end

puts stringy(6)
puts stringy(9, 1)
