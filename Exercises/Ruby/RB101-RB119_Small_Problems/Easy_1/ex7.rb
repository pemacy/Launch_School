# frozen_string_literal: true

def mad_lib
  p 'Enter a noun: '
  noun = gets.chomp
  p 'Enter a verb: '
  verb = gets.chomp
  p 'Enter an adjective: '
  adj = gets.chomp
  p 'Enter and adverb: '
  adv = gets.chomp

  puts "Do you #{verb} your #{adj} #{noun} #{adv}? That's hilarious!"
end

mad_lib
