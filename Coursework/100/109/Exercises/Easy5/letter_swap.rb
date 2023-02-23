def swap(words)
  temp = ''
  words = words.split
  words.each do |el|
    el[0], el[-1] = el[-1], el[0]
  end
  words.join(' ')
end

p swap('Oh what a wond')
