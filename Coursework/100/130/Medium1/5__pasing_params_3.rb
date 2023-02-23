items = ['apples', 'corn', 'cabbage', 'wheat']

def gather(items)
  puts "Let's start gathering food."
  yield(items)
  puts "We've finished gathering!"
  puts "\n\n"
end

gather(items) do | *produce, whet|
  puts "#{produce.join(", ")}"
  puts "#{whet}"
end

gather(items) do | first, *middle, last |
  puts "#{first}"
  puts "#{middle.join(", ")}"
  puts "#{last}"
end

gather(items) do | first, *last |
  puts "#{first}"
  puts "#{last.join(", ")}"
end

gather(items) do |first, second, third, fourth|
  puts "#{first}, #{second}, #{third}, #{fourth}"
end
