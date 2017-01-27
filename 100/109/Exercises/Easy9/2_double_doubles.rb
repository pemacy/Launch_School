def twice(num)
  len = num.to_s.size.to_f
  left_side = num.to_s[0..len / 2 - 1].to_i
  rt_side = num.to_s[(len / 2).ceil..-1].to_i

  if left_side == rt_side
    return num
  else
    return num *= 2
  end
end

p twice(103103) == 103103
