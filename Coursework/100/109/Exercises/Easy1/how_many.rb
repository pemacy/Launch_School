# MY ORIGINAL STAB AT IT
def count_occurrences(vehicles)
  number_of_each = {}
  vehicles.each do |vehicle|
    number_of_each[vehicle] += 1
  end
  number_of_each
end

# LAUNCH SCHOOL WAY
def count_launch(vehicle)
  occurances = {}
  vehicle.uniq.each do |veh|
    occurances[veh] = vehicle.count(veh)
  end
  occurances
end

# A COOL SOLUTION
def cool_solution(vehicles)
  vehicles.each_with_object(Hash.new(0)) do |vehicle, count|
    count[vehicle] += 1
  end
end

# FETCH SOLUTION
def fetch_solution(veh)
  count =  Hash.new(0)
  veh.size.times do |index|
    item = veh[index]
    count[item] += 1
  end
  count
end


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck', 'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles).each { | k,v | puts "#{k} => #{v}"}
# count_launch(vehicles).each { | k,v | puts "#{k} => #{v}"}
cool_solution(vehicles).each { | k,v | puts "#{k} => #{v}"}
fetch_solution(vehicles).each { | k,v | puts "#{k} => #{v}"}
