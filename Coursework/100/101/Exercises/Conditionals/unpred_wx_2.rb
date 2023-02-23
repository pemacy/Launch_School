sun = ['visible', 'hidden'].sample

puts "The clouds are blocking the sun!" unless sun.eql?('visible')
