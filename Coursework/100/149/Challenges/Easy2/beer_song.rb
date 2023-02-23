class BeerSong
  def verse(bottle)
    if bottle > 1
      "#{bottle} bottles of beer on the wall, #{bottle} bottles of beer.\n" \
      "Take one down and pass it around, #{bottle - 1} #{bottle > 2 ? "bottles" : "bottle"} of beer on the wall.\n"
    elsif bottle == 1
      "#{bottle} bottle of beer on the wall, #{bottle} bottle of beer.\n" \
      "Take it down and pass it around, no more bottles of beer on the wall.\n"
    else
      "No more bottles of beer on the wall, no more bottles of beer.\n" \
      "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
    end
  end

  def lyrics
    verses(99,0)
  end

  def verses(start, stop)
    song = []
    while start >= stop do
      song << verse(start)
      start -= 1
    end
    song.join("\n")
  end
end

# class BeerSong
#   def initialize
#     @song = generate_song
#   end
#
#   def generate_song
#     song = []
#     song << "No more bottles of beer on the wall, no more bottles of beer.\n" \
#             "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
#     song << "1 bottle of beer on the wall, 1 bottle of beer.\n" \
#             "Take it down and pass it around, no more bottles of beer on the wall.\n"
#     song << "2 bottles of beer on the wall, 2 bottles of beer.\n" \
#             "Take one down and pass it around, 1 bottle of beer on the wall.\n"
#
#     3.upto(99) do |beers|
#       song << "#{beers} bottles of beer on the wall, #{beers} bottles of beer.\n" \
#               "Take one down and pass it around, #{beers - 1} bottles of beer on the wall.\n"
#     end
#     song
#   end
#
#   def verse(verse_number)
#     @song[verse_number]
#   end
#
#   def verses(first_verse, last_verse)
#     @song[last_verse..first_verse].reverse.join("\n")
#   end
#
#   def lyrics
#     verses(99, 0)
#   end
# end

# puts BeerSong.new.lyrics
# puts BeerSong.new.verses(99, 98)
