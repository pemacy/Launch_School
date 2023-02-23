def palindromic_number?(num)
  num == num.to_s.reverse.to_i
end

p palindromic_number?(12321)
