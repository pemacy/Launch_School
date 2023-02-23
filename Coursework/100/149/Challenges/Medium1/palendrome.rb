class Palendrome
  def initialize(str)
    @str = str.downcase
  end

  def determine_if_palendrome
    remove_non_letters
    test_opposites
  end

  def remove_non_letters
    @palen = @str.chars.map{|e| e if e.count('a-z') > 0}.join
    @size = @palen.size
  end

  def test_opposites
    0.upto(@size/2){|i| return false if (@palen[i] != @palen[@size-1-i])}
    true
  end
end

pa = Palendrome.new("go hang a salami, i'm a lasagna hog")
p pa.determine_if_palendrome
