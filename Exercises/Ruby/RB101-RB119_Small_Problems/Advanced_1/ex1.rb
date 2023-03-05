# frozen_string_literal: true

# Let's build another program using madlibs. We made a program like this in
# the easy exercises. This time, the requirements are a bit different.

# Make a madlibs program that reads in some text from a text file that you
# have created, and then plugs in a selection of randomized nouns, verbs,
# adjectives, and adverbs into that text and prints it. You can build your
# lists of nouns, verbs, adjectives, and adverbs directly into your program,
# but the text data should come from a file or other external source. Your
# program should read this text, and for each line, it should place random
# words of the appropriate types into the text, and print the result.

REPLACEMENT_WORDS = {
  adjective: %w[quick lazy sleepy ugly],
  noun: %w[fox dog head leg],
  verb: %w[jumps lifts bites licks],
  adverb: %w[easily lazily noisily excitedly]
}.freeze

def madlibs(file)
  text = File.open(file)
  text = text.readlines.each_with_object([]) do |line, new_line|
    line = line.gsub('%{adjective}', REPLACEMENT_WORDS[:adjective].sample)
    line = line.gsub('%{noun}', REPLACEMENT_WORDS[:noun].sample)
    line = line.gsub('%{verb}', REPLACEMENT_WORDS[:verb].sample)
    line = line.gsub('%{adverb}', REPLACEMENT_WORDS[:adverb].sample)
    new_line << line
  end
  puts text
end

madlibs('madlib_data.txt')
