def short_long_short(str1, str2)
  str1.size < str2.size ? str1.concat(str2.concat(str1)) : str2.concat(str1.concat(str2))
end

puts short_long_short('abc','defgh')
