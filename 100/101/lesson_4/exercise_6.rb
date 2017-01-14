# Given the following data structure and without modifying the original array, use the map method to return a new array identical in structure to the original but where the value of each integer is incremented by 1.

arr = [{a: 1}, {b: 2, c: 3}, {d: 4, e: 5, f: 6}]

arr.map do |el|
  if el.map{|_,v| v}.[0]
    el.map{|_,v| v += 1}
  else
    el.map do |sub_el|
      if sub_el.map{|_,v| v}[0]
        sub_el.map{|_,v| v += 1}
      else

 arr.map{|hash| hsh={} hash.map {|k,v| hsh[k] = v + 1} hsh }
