(1..99).each_with_index do | n,i |
  if i != 0 && i != (1..99).size-1
    puts "#{n}" if n.odd?
  end
end

1.upto(98) { |i| p i if i.odd?}

a = (1..98).select { |num| num if num.odd?}
print a
