require 'pry'

class PigLatin
  VOWELS = %w(a e i o u)

  def self.translate(phrase)
    phrase.split(' ').map do |word|
      translate_word(word) + 'ay'
    end.join(' ')
  end

  def self.translate_word(word)
    if begins_with_vowel_sound(word)
      word
    else
      parse_consonants(word)
    end
  end

  def self.begins_with_vowel_sound(word)
    word.match(/\A[aeiou]+.*|y[^aeiou].*|xr.*/i)
  end

  def self.parse_consonants(word)
    split_consts = /\A([^aeiou]*qu|th[^aeiou]*|[^aeiou]*)(.*)/i.match(word)
    split_consts[2] + split_consts[1]
  end
end

# p PigLatin.translate('squid yfast run apple taple xray')


class PigLatinTryOne
  VOWELS = %w(a e i o u)

  def self.translate(str)
    @phrase = str.split
    @vowel = get_first_vowel
    scrub_first_vowel
    move_first_letters.map { |e| e + 'ay' }.join(' ')
  end

  def self.get_first_vowel
    @phrase.each_with_object([]) do |word, arr|
      arr << find_first_vowel(word)
    end
  end

  def self.find_first_vowel(word)
    for chr in word.chars
      return word.chars.index(chr) if VOWELS.include?(chr)
    end
  end

  def self.scrub_first_vowel
    @vowel.map!.with_index do |v, idx|
      if !@phrase[idx].scan(/qu/).empty?
        v + 1
      elsif @phrase[idx].chars.first == 'y' && !VOWELS.include?(@phrase[idx][1])
        0
      elsif @phrase[idx][0,2] == 'xr'
        0
      else
        v
      end
    end
  end

  def self.change(word, idx)
    case
    when @vowel[idx] == 0 then word
    when @vowel[idx] > 0 then word[@vowel[idx]..-1] + word[0..(@vowel[idx] - 1)]
    end
  end

  def self.move_first_letters
    @phrase.map.with_index do |word, idx|
      @vowel[idx].zero? ? word : change(word, idx)
    end
  end
end

p PigLatinTryOne.translate('squid yfast run apple')
