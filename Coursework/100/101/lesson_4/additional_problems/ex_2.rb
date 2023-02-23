# Add up all of the ages from the Munster family hash:

ages = { "Herman" => 32, "Lily" => 30, "Grandpa" => 5843, "Eddie" => 10, "Marilyn" => 22, "Spot" => 237 }

age = 0
ages.each do |_,v|
  age += v
end
puts age

age2 = ages.values.inject do |sum, el|
  sum + el
end

puts age2
# def age(&block)
#   puts yield a
# end
#
# age do
