print "Please write a word or multiple words: "
input = gets.chomp
puts "There are #{input.split.join('').size} characters in \"#{input}\""
