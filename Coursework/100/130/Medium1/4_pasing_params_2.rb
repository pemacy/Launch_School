arr =%w(raven finch hawk eagle)

def birds(arr)
  yield(arr)
end

birds(arr) do |raven, finch, *birds_of_prey|
  puts birds_of_prey
end
