def encrypt(str)
  str.each_char.reduce('') do |result, n|
    case n
    when 'a'..'m', 'A'..'M' then result.concat(n.ord + 13)
    when 'n'..'z', 'N'..'Z' then result.concat(n.ord - 13)
    else
      result.concat(n)
    end
  end
end

p encrypt('Nqn Ybirynpr')

# uppercase - 65-90
# lowercase - 97 - 122


# str.codepoints.each do |n|
#   case n
#   when 65..77
#     new_string.concat(n + 13)
#   when 78..90
#     new_string.concat(n - 13)
#   when 97..109
#     new_string.concat(n + 13)
#   when 110..122
#     new_string.concat(n - 13)
#   else
#     new_string.concat(n)
#   end
# end
