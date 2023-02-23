# frozen_string_literal: true

# Write a method named greet that invokes the following methods:

def hello
  'Hello'
end

def world
  'World'
end

def greet
  "#{hello} #{world}"
end

puts greet
