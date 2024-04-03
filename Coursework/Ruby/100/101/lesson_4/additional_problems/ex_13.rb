# A UUID is a type of identifier often used as a way to uniquely identify items...which may not all be created by the same system. That is, without any form of synchronization, two or more separate computer systems can create new items and label them with a UUID with no significant chance of stepping on each other's toes.
#
# It accomplishes this feat through massive randomization. The number of possible UUID values is approximately 3.4 X 10E38.
#
# Each UUID consists of 32 hexadecimal characters, and is typically broken into 5 sections like this 8-4-4-4-12 and represented as a string.
#
# It looks like this: "f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91"
#
# Write a method that returns one UUID when called with no parameters.

def generate_UUID_1
  uuid = ''
  hex_index = (0..15)
  hex_values = ('0'..'9').to_a + ('a'..'f').to_a

  (0..8).each do |num|
    uuid << hex_values[rand(hex_index)]
  end
  uuid << '-'
  (0..4).each do |num|
    uuid << hex_values[rand(hex_index)]
  end
  uuid << '-'
  (0..4).each do |num|
    uuid << hex_values[rand(hex_index)]
  end
  uuid << '-'
  (0..12).each do |num|
    uuid << hex_values[rand(hex_index)]
  end
  uuid
end


# Better way
def generate_UUID_2
  uuid = ''
  hex_index = (0..15)
  hex_values = ('0'..'9').to_a + ('a'..'f').to_a
  sections = [8,4,4,4,12]

  sections.each_with_index do |num, i|
    num.times { uuid << hex_values[rand(hex_index)]}
    uuid << '-' unless i == sections.size - 1
  end
  uuid
end

puts generate_UUID_2