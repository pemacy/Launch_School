class MagicString < String
  def ~
    tr 'A-Za-z', 'N-ZA-Mn-za-m'
  end
end

str = MagicString.new('This is my String')
