def longest(file)
  text = IO.read(file)
  sentences = text.split('.')
  sentences = sentences.map { |per| per.split('?') }.flatten
  sentences = sentences.map { |per| per.split('!') }.flatten

  r = []
  sentences.each { |s| r = s if s.size > r.size }
  puts "The longest sentence in this book is #{r.split.size} words long"
end

file = File.open('pg84.txt')
longest(file)
file.close
