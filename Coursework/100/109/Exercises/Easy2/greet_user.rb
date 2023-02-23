def greeting(name)
  return "HELLO #{name.chop.upcase}. WHY ARE WE SCREAMING?" if name.end_with?('!')
  "Helo #{name.capitalize}."
end

print "What is your name?  "
name = gets.chomp
puts greeting(name)
