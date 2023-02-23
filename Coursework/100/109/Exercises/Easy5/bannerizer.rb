def print_in_box(message)
  puts "+-#{'-' * message.size}-+"
  puts "| #{' ' * message.size} |"
  puts "| #{message} |"
  puts "| #{' ' * message.size} |"
  puts "+-#{'-' * message.size}-+"
end

print_in_box('')


def print_in_box_wrap(message)
  message_wrap = []
  number_of_wraps = message.size / (80) + 1

  chars_per_line, remainder = message.size.divmod(number_of_wraps)
  buffer = chars_per_line

  number_of_wraps.times do |n|
    message_wrap[n] = message[(chars_per_line * (n))..(chars_per_line * (n+1)-1)]
  end
  message_wrap_size = message.size - message_wrap.map{|n| n.size}.reduce(:+)
  last_line_buffer = ' ' * (buffer - message_wrap_size)
  last_line = message[(message.size - message_wrap_size)..-1] + last_line_buffer
  message_wrap << last_line if message_wrap_size > 0

  puts "+-#{'-' * buffer}-+"
  puts "| #{' ' * buffer} |"
  message_wrap.each {|msg| puts "| #{msg} |"}
  puts "| #{' ' * buffer} |"
  puts "+-#{'-' * buffer}-+"
end

print_in_box_wrap('Write a method that takes a floating point number that represents an angle between 0 and 360 degrees and return Write a method that takes a floating poietw')
