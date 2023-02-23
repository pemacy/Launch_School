CONVERT = {
  '0' => 0, '1' => 1, '2' => 2, '3' => 3, '4' => 4, '5' =>5,
  '6' => 6, '7' => 7, '8' => 8, '9' => 9, 'a' => 10, 'b' => 11,
  'c' => 12, 'd' => 13, 'e' => 14, 'f' => 15
}

def string_to_i(str)
  str = str.chars
  sign = str.shift if str.include?('+') || str.include?('-')
  ints = str.map { |chr| CONVERT[chr] }.reverse
  sum = 0
  ints.each_with_index { |el, i| sum += el * (10 ** i)}
  sign == '-'? sum * -1 : sum
end

p string_to_i("-1234")
