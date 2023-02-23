CONVERT = {
  '0' => 0, '1' => 1, '2' => 2, '3' => 3, '4' => 4, '5' =>5,
  '6' => 6, '7' => 7, '8' => 8, '9' => 9, 'a' => 10, 'b' => 11,
  'c' => 12, 'd' => 13, 'e' => 14, 'f' => 15
}


def string_to_i(str)
  ints = str.chars.map { |chr| CONVERT[chr] }.reverse
  sum = 0
  ints.each_with_index { |el, i| sum += el * (10 ** i)}
  sum
end

p string_to_i("1234") + 1

def hex_to_int(str)
  str.downcase!
  hex = str.chars.map { |c| CONVERT[c] }.reverse

  sum = 0
  hex.each_with_index { |el,i| sum += el * (16 ** i) }
  sum
end

p hex_to_int('4d9f')
