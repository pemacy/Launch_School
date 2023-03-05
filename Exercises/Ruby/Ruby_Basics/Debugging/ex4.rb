# frozen_string_literal: true

# Magdalena has just adopted a new pet! She wants to add her new dog, Bowser, to
# the pets hash. After doing so, she realizes that her dogs Sparky and Fido have
# been mistakenly removed. Help Magdalena fix her code so that all three of her
# dogs' names will be associated with the key :dog in the pets hash.

pets = { cat: 'fluffy', dog: ['sparky', 'fido'], fish: 'oscar' }

pets[:dog] = 'bowser'

p pets #=> {:cat=>"fluffy", :dog=>"bowser", :fish=>"oscar"}

# => pets[:dog] replaces the old value with the new value
# to add 'bowser' to the array you need to push it via pets[:dog] << 'bowser'
