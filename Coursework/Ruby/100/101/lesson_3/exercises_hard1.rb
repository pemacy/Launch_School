# =====================================================================
# Problem 1 - fix code so it returns false condition if ia_an_ip_number is false
# if the ip address is other than 4 sections (1.1.1.1) need to return invalid

def dot_separated_ip_address?(input_string)
  dot_separated_words = input_string.split(".")
  # return "Invalid" if dot_separated_words.length != 4
  while dot_separated_words.size > 0 do
    word = dot_separated_words.pop
    return false unless is_an_ip_number?(word)
  end
  return true
end
