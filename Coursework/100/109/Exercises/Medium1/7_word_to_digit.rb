DIGITS_DICT = {zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5,
              six: 6, seven: 7, eight: 8, nine: 9}

def word_to_digit(str)
  result = str.split.map do |word|
    word.gsub!(/\w+/) do |item|
      DIGITS_DICT.keys.include?(item.to_sym) ?
        DIGITS_DICT[item.to_sym].to_s : item
      end
  end.join(' ')
  result.gsub!(/(\d)\s/,'\1')
end

def phone_num(str)
  seven_digit = /(\d{3})(\d{4})/
  ten_digit = /(\d{3})(\d{3})(\d{4})/

  str.gsub!(ten_digit,'(\1)\2-\3')
  str.gsub!(seven_digit, '(\1)\2')
  str
end

p phone_num(word_to_digit('Please call me at 332 five five five one two three four. Thanks.'))
