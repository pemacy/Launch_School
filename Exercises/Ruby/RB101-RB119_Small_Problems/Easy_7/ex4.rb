# frozen_string_literal: false

# Write a method that takes a string as an argument and returns a new string in
# which every uppercase letter is replaced by its lowercase version, and every
# lowercase letter by its uppercase version. All other characters should be
# unchanged.

# You may not use String#swapcase; write your own version of this method.

def swapcase(str)
  str.codepoints.each_with_object('') do |asci_num, new_str|
    case asci_num
    when (97..122) then new_str << (asci_num - 32).chr
    when (65..90) then new_str << (asci_num + 32).chr
    else
      new_str << asci_num.chr
    end
  end
end

puts swapcase('CamelCase') == 'cAMELcASE'
puts swapcase('Tonight on XYZ-TV') == 'tONIGHT ON xyz-tv'
