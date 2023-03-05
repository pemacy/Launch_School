# frozen_string_literal: true

# Write a program that prints out groups of words that are anagrams. Anagrams
# are words that have the same exact letters in them but in a different order.
# Your output should look something like this:

def anagram(arr)
  anagrm = arr.each_with_object({}) do |word, hsh|
    sorted_letters = word.chars.sort.join
    hsh[sorted_letters] ||= []
    hsh[sorted_letters] << word
  end
  anagrm.values.select { |arr| arr.size > 1 }
end

words =  ['demo', 'none', 'tied', 'evil', 'dome', 'mode', 'live',
          'fowl', 'veil', 'wolf', 'diet', 'vile', 'edit', 'tide',
          'flow', 'neon']

anagram(words).each { |arr| p arr }
