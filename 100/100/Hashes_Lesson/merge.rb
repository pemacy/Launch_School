# merge.rb

h1 = { 1=> 'One', 2=> 'Two' }
h2 = { 3=> 'Three', 4=> 'Four' }

puts h1.to_s + '   ' + h2.to_s
puts h1.merge(h2)

puts h1.to_s + '   ' + h2.to_s

puts h1.merge!(h2)
puts h1.to_s + '   ' + h2.to_s
