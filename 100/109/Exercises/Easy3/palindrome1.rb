def palindrome?(str)
  str == str.reverse
end

def array_palindrome?(arr)
  arr == arr.reverse
end

p palindrome?("madam i'm adam")
