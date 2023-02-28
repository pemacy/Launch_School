# frozen_string_literal: true

# We wrote a neutralize method that removes negative words from sentences.
# However, it fails to remove all of them. What exactly happens?

def neutralize(sentence)
  words = sentence.split(' ')
  no_neg = [] # solution
  words.each do |word|
    # words.delete(word) if negative?(word) # original
    no_neg << word unless negative?(word) # solution
  end

  # words.join(' ') # original
  no_neg.join(' ')
end

def negative?(word)
  [ 'dull',
    'boring',
    'annoying',
    'chaotic'
  ].include?(word)
end

puts neutralize('These dull boring cards are part of a chaotic board game.')
# Expected: These cards are part of a board game.
# Actual: These boring cards are part of a board game.


