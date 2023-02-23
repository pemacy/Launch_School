# greeting.rb
def greeting(name)
  "Good evening " + name
end

p "Enter a name: "
name = gets.chomp
puts greeting(name)
