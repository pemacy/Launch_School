# frozen_string_literal: true

# Take a look at the following code:
name = 'Bob'
save_name = name
name = 'Alice'
puts name, save_name

# What does this code print out? Think about it for a moment before continuing.

# If you said that code printed

# Alice
# Bob

# you are 100% correct, and the answer should come as no surprise. Now, let's
# look at something a bit different:

name = 'Bob'
save_name = name
name.upcase!
puts name, save_name

# => explain the results: both name and save_name point to the same object
# when you mutate an object, all the variables that point to the object will
# also return the changes, since the object itself is changed, so everything
# pointing to that object will return the changes
