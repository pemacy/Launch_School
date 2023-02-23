def is_odd?(num)
  num.abs.remainder(2) == 1
end

puts is_odd?(-3)
