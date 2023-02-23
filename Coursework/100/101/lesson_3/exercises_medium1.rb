def factors(number)
  dividend = number
  divisors = []
  while dividend > 0 do
    divisors << number / dividend if number % dividend == 0
    dividend -= 1
  end
  divisors
end

puts factors(-5)

# =====================================================================
# Problem 6

def tricky_method(a_string_param, an_array_param)
  a_string_param += "rutabaga"
  an_array_param << "rutabaga"
end

my_string = "pumpkins"
my_array = ["pumpkins"]
tricky_method(my_string, my_array)

puts "My string looks like this now: #{my_string}"
puts "My array looks like this now: #{my_array}"
puts " "


# Refactored to make it easier to read
def not_so_tricky_method(a_string_param, an_array_param)
  a_string_param += "rutabaga"
  an_array_param += ["rutabaga"]

  return a_string_param, an_array_param
end

my_string = "pumpkins"
my_array = ["pumpkins"]
my_string, my_array = not_so_tricky_method(my_string, my_array)

puts "My string looks like this now: #{my_string}"
puts "My array looks like this now: #{my_array}"
puts " "

# Every language (Ruby included) provides ways and means of writing "clever"
# code that depends on some of the less obvious traits of the language.

# Every good programmer practices these tricks...and then avoids them
# like the plague.

# Clever programmers don't write "clever" code. They write explicit code
# that is easy to read, debug and modify as the requirements change.

# =====================================================================
# Problem 7

answer = 42

def mess_with_it(some_number)
  some_number += 8
end

new_answer = mess_with_it(answer)

p answer - 8
puts " "

# =====================================================================
# Problem 8 - don't understand how a hash will mutate if another variable set to hash is changed

munsters = {
  "Herman" => { "age" => 32, "gender" => "male" },
  "Lily" => { "age" => 30, "gender" => "female" },
  "Grandpa" => { "age" => 402, "gender" => "male" },
  "Eddie" => { "age" => 10, "gender" => "male" },
  "Marilyn" => { "age" => 23, "gender" => "female"}
}

def mess_with_demographics(demo_hash)
  demo_hash["Herman"]["age"]=102
  demo_hash = {
    "Herman" => { "age" => 13, "gender" => "male" },
    "Lily" => { "age" => 13, "gender" => "female" },
    "Grandpa" => { "age" => 13, "gender" => "male" },
    "Eddie" => { "age" => 13, "gender" => "male" },
    "Marilyn" => { "age" => 13, "gender" => "female"}
  }
  [demo_hash, demo_hash.object_id]
end

puts "#{munsters}   #{munsters.object_id}"
puts " "
puts mess_with_demographics(munsters)[0].to_s + "  " + mess_with_demographics(munsters)[1].to_s
puts " "
puts "#{munsters}   #{munsters.object_id}"
puts " "
