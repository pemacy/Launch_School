def madlibs(hsh)
  "Do you #{hsh[:verb]} your #{hsh[:adj]} #{hsh[:noun]} #{hsh[:adv]}."
end

hsh = {verb: '', noun: '', adj: '', adv: ''}
print "Enter a noun "
hsh[:noun] = gets.chomp
print "Enter a verb "
hsh[:verb] = gets.chomp
print "Enter an adjective "
hsh[:adj] = gets.chomp
print "Enter a adverb "
hsh[:adv] = gets.chomp

puts madlibs(hsh)
