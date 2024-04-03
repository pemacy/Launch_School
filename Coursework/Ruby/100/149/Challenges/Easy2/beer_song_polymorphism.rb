class Verse0
  def self.verse(_)
    "No more bottles of beer on the wall, no more bottles of beer.\n" \
    "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
  end
end

class Verse1
  def self.verse(_)
    "1 bottle of beer on the wall, 1 bottle of beer.\n" \
    "Take it down and pass it around, no more bottles of beer on the wall.\n"
  end
end

class Verse2
  def self.verse(_)
    "2 bottles of beer on the wall, 2 bottles of beer.\n" \
    "Take one down and pass it around, 1 bottle of beer on the wall.\n"
  end
end

class VerseN
  def self.verse(bottles)
    "#{bottles} bottles of beer on the wall, #{bottles} bottles of beer.\n" \
    "Take one down and pass it around, #{bottles - 1} bottles of beer on the wall.\n"
  end
end

class BeerSong
  VERSE_CLASSES = [Verse0, Verse1, Verse2].freeze

  def verse(start, finish = start)
    song = []
    start.downto(finish) do |bottles|
      song << VERSE_CLASSES.fetch(bottles, VerseN).verse(bottles)
    end
    song.join("\n")
  end

  alias verses verse

  def lyrics
    verse(99,0)
  end
end

puts BeerSong.new.verse(99)
