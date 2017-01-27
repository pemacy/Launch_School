def swapcase(str)
  camel_case = []
  str.chars.map do |chr|
    camel_case << chr.upcase if /[a-z]/ =~ chr
    camel_case << chr.downcase if /[A-Z]/ =~ chr
    camel_case << chr.downcase if /[^A-Za-z]/ =~ chr
  end
  camel_case.join
end

p swapcase('Tonight on XYZ-TV')
