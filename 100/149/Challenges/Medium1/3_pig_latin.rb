binding.pry

class PigLatin
  VOWELS = %w(a e i o u)

  def self.translate(str)
    @str = str
    deterimine_first_letter
    @str + 'ay'
  end

  def deterimine_first_letter
    case
    when VOWELS.include?(@str[0])
      s
      asd
