# This class implements the abash cypher
class Atbash
  FIRST = %w(a b c d e f g h i j k l m).freeze
  SECOND = %w(z y x w v u t s r q p o n).freeze

  class << self
    def encode(str)
      @converter = []
      @str = str.downcase.split.join
      convert
      segment = '(.{5})' * (@converter.size / 5)
      @converter.join('').match(/#{segment}(\w*)/).captures.join(' ').strip
    end

    def convert
      @str.chars.each do |c|
        next if c =~ /\W/ || c == '_'
        if c =~ /\d/
          @converter << c
          next
        end
        @converter << SECOND[FIRST.index(c)] if FIRST.include?(c)
        @converter << FIRST[SECOND.index(c)] if SECOND.include?(c)
      end
    end
  end
end

# ----- Code Process -----
# Letter Substitution
#   My going in gameplan was to use an index lookup between two arrays to find
#   which array housed the character, and what was that index so I could look it
#   up in the other array.  This method worked very well first try and so I kept
#   it.
#
# Other Problems Not Planned For
#   Character is not in the arrays
#     Originally I planned to not hold anything in the converter array unless
#     it matched with something in one of the constant arrays:
#
#       next unless FIRST.include?(c) && SECOND.include?(c)
#
#     so it would proceed to the next 'a-z' character if it found a non
#     alphabetic character.  After looking at the test suite, I realized I
#     needed to account for numbers, and then used REGEXP to weed out any non
#     alpha-numeric characters.
#
#     Spaces after 5 characters
#       I didn't account for this at first either, but after seeing the later
#       test suite tests I realized that the pattern it is looking for is to
#       have a space after 5 characters.  This proved to be more difficult
#       that I realized.  At first I used the iterator 'each_with_index':
#
#         converter << ' ' if (idx % 5).zero? && idx > 0
#
#       but then realized that if I skipped over any characters, idx would
#       increment and it wouldn't necessarily keep track of 5 characters added
#       to the converter array. What I needed was a way to count the characters
#       in the converter array, and insert a space after 5 characters.  So I
#       made another iterator after the converter array was full which was:
#
#         converter.each_with_index { |c,idx| converter.insert(i,' ') if
#                                             (idx % 5).zero? && idx > 0 }
#
#       But this also proved ineffective since it would change the array as I
#       was iterating over it.  So I ended up using REGEXP and to match all
#       occurances of 5 character segments and join them with a space:
#
#         segments = "(.{5})" * (converter.size / 5)
#         converter.join('').match(/#{segments}(\w*)/).captures.join(' ').strip
