# print_keys_and_values.rb

h1 = { 1=> 'One', 2=> 'Two', 3=> 'Three', 4=> 'Four' }

h1.each_key {|k| puts k}

h1.each_value{|v| puts v}

h1.each {|k, v| puts "Key '#{k}' = Value '#{v}'"}
