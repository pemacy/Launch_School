# Create a hash that expresses the frequency with which each letter occurs in this string:

statement = "The Flintstones Rock"

# ex: { "F"=>1, "R"=>1, "T"=>1, "c"=>1, "e"=>2, ... }

hsh = {}

statement.chars.each do |el|
  hsh[el] = hsh[el] + 1 if hsh[el]
  hsh[el] = 1 unless hsh[el]
end

p hsh.sort

# Another way:
result = {}
letters = ('A'..'Z').to_a + ('a'..'z').to_a
letters.each do |letter|
  letter_frequency = statement.scan(letter).count
  result[letter] = letter_frequency if letter_frequency > 0
end
