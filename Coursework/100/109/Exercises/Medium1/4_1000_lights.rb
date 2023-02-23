def test_lights(switches)
  switches.map.with_index{|switch, index| index + 1 if switch}.delete_if{|el| el == nil}
end

def lights(num_lights, num_times)
  switches = Array.new(num_lights, false)
  counter = 1
  loop do
    switches.map!.with_index do | bool,index |
      (index + 1) % counter == 0 ? !bool : bool
    end
    puts "#{switches} #{counter}"
    counter += 1
    break if counter > num_times
  end
  test_lights(switches)
end

p lights(5,5)
