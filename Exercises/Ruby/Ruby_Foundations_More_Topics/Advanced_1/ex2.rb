# frozen_string_literal: true

# For this exercise, we'll be learning and practicing our knowledge of the arity of lambdas, procs, and implicit blocks. Two groups of code also deal with the definition of a Proc and a Lambda, and the differences between the two. Run each group of code below: For your answer to this exercise, write down your observations for each group of code. After writing out those observations, write one final analysis that explains the differences between procs, blocks, and lambdas.

# Group 1
my_proc = proc { |thing| puts "This is a #{thing}." }
puts my_proc
puts my_proc.class
my_proc.call
my_proc.call('cat')
my_proc.call('cat', 'dog')

# Procs don't require matching arguments, it will disregard more extra arguments, and make variables nil if they are not given as arguments

puts 'Group 1 complete, continue?'
cont = gets.chomp
return if cont == 'n'

# Group 2
my_lambda = lambda { |thing| puts "This is a #{thing}." }
my_second_lambda = -> (thing) { puts "This is a #{thing}." }
puts my_lambda
puts my_second_lambda
puts my_lambda.class
my_lambda.call('dog')

begin
  my_lambda.call
rescue ArgumentError => m
  puts m.message
end

begin
  my_third_lambda = Lambda.new { |thing| puts "This is a #{thing}." }
rescue NameError => m
  puts m.message
end

# Lambdas require the correct number of arguments when called or they will throw an error

puts 'Group 2 complete, continue?'
cont = gets.chomp
return if cont == 'n'

# Group 3
def block_method_1(animal)
  yield if block_given?
end

block_method_1('seal') { |seal| puts "This is a #{seal}."}
block_method_1('seal')

# yield requires a non-explicit block (or explicit) given or it will throw an error, use 'if block_given?' to guard against a non-explicit block being given to a method if you think that may be an issue

puts 'Group 3 complete, continue?'
cont = gets.chomp
return if cont == 'n'

# Group 4
def block_method_2(animal)
  yield(animal)
end

block_method_2('turtle') { |turtle| puts "This is a #{turtle}."}
block_method_2('turtle') do |turtle, seal|
  puts "This is a #{turtle} and a #{seal}."
end

block_method_2('turtle') { puts "This is a #{animal}."} # => error: animal undefined

# if a variable is called in a block, it must be defined between the vertical lines
