def palindrome?(str)
  str = str.downcase.chars.keep_if{ |v| v =~ /a-z/ }.join('')
  str == str.reverse
end

p palindrome?("Madam i'm adam")

# launch school answer
def real_palindrome?(string)
  string = string.downcase.delete('^a-z0-9')
  palindrome?(string)
end
