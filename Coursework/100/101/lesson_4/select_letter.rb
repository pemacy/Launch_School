# select_letter.rb

puts "Enter a string and a letter to determine how many times that letter
appears in the string"

puts "String: "
str = gets.chomp.downcase
puts "Letter: "
letter = gets.chomp.downcase

def select_letter(str, letter)
  counter = 0
  letter_count = 0
  until counter == str.size
    if str[counter] == letter
      letter_count += 1
    end
    counter += 1
  end
  letter_count
end

puts "#{letter} appears #{select_letter(str, letter)} times"
