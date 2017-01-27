def remove_vowels(str_arr)
  str_arr.map { |str| str.gsub(/[aeiou]/i, '')}
end

p remove_vowels(%w(ABC AEIOU XYZ))
