# Given this data structure, and without using the Array#flatten method, write some code to return a new array containing all of the items in the original array but in a flat structure.

arr = [['stars', 'river'], 'letter', ['leaves', ['horses', 'table']]]

flat = arr.each_with_object([]) do |el, flat|
  if el.class == String
    flat.push(el)
  else
    el.each do |el|
      if el.class == String
        flat.push(el)
      else
        el.each { |el| flat.push(el)}
      end
    end
  end
end

p flat
