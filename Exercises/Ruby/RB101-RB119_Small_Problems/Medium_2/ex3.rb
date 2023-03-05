# frozen_string_literal: true

# In the easy exercises, we worked on a problem where we had to count the
# number of uppercase and lowercase characters, as well as characters that
# were neither of those two. Now we want to go one step further.

# Write a method that takes a string, and then returns a hash that contains 3
# entries: one represents the percentage of characters in the string that are
# lowercase letters, one the percentage of characters that are uppercase
# letters, and one the percentage of characters that are neither.

# You may assume that the string will always contain at least one
# character.

def letter_case_count(str)
  hsh = str.codepoints.each_with_object(Hash.new(0)) do |asci_num, count_hsh|
    case asci_num
    when (97..122) then count_hsh[:lowercase] += 1
    when (65..90) then count_hsh[:uppercase] += 1
    else
      count_hsh[:neither] += 1
    end
  end
  { lowercase: hsh[:lowercase],
    uppercase: hsh[:uppercase],
    neither: hsh[:neither] }
end

def letter_percentages(str)
  num_letters = str.size.to_f
  case_count = letter_case_count(str)
  case_count.each_with_object({}) do |(type, count), hsh|
    hsh[type] = (count / num_letters) * 100
  end
end

p letter_percentages('abCdef 123') == { lowercase: 50.0, uppercase: 10.0, neither: 40.0 }
p letter_percentages('AbCd +Ef') == { lowercase: 37.5, uppercase: 37.5, neither: 25.0 }
p letter_percentages('123') == { lowercase: 0.0, uppercase: 0.0, neither: 100.0 }
