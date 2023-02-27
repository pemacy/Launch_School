# frozen_string_literal: true

# A collection of spelling blocks has two letters per block, as shown in this
# list:

# This limits the words you can spell with the blocks to just those words that
# do not use both letters from any given block. Each letter in each block can
# only be used once.

# Write a method that returns true if the word passed in as an argument can be
# spelled from this set of blocks, false otherwise.

BLOCKS = { 'B' => 'O', 'X' => 'K', 'D' => 'Q', 'C' => 'P', 'N' => 'A',
           'G' => 'T', 'R' => 'E', 'F' => 'S', 'J' => 'W', 'H' => 'U',
           'V' => 'I', 'L' => 'Y', 'Z' => 'M' }.freeze

def block_word?(str)
  letters = str.chars
  BLOCKS.none? do |chr_1, chr_2|
    letters.include?(chr_1) && letters.include?(chr_2)
  end
end

p block_word?('BATCH') == true
p block_word?('BUTCH') == false
p block_word?('jest') == true
