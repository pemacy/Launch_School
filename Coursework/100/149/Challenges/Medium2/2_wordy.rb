class WordProblem
  OPERATORS = {'plus'=>:+, 'minus'=>:-, 'divide'=>:/, 'mult'=>:*}

  def initialize(str)
    @str = str
  end

  def answer
    parse_string
    # get_result
    get_result_adv
  end

  private

  def parse_string
    @ops = @str.scan(/(#{OPERATORS.keys.join('|')})/).flatten.map! { |o| OPERATORS[o]}
    @nums = @str.scan(/(-?\d+)/).flatten.map!(&:to_i)
    raise ArgumentError if @ops.empty? || @nums.empty? || @nums.size != @ops.size + 1
  end

  def get_result_adv
    @ops.each_with_index.reduce(@nums.first) do |result,(op, idx)|
      result.send op, @nums[idx + 1]
    end
  end

  def get_result
    @ops.map do |o|
      result = @nums[0..1].reduce(o)
      @nums.slice!(0..1)
      @nums.unshift(result)
      result
    end.last
  end
end

word = WordProblem.new('-4 plus by 8 plus 32')
p word.answer

# class WordProblem
#   OPERATORS = {'plus'=>:+, 'minus'=>:-, 'divide'=>:/, 'mult'=>:*}
#
#   def initialize(str)
#     @str = str
#     @nums = []
#     @ops = []
#   end
#
#   def answer
#     eval(parse_string)
#   end
#
#   private
#
#   def parse_string
#     parse = @str.scan(/(-?\d+|#{OPERATORS.keys.join('|')})/).flatten
#     parse.join(' ').gsub(/#{OPERATORS.keys.join('|')}/){ OPERATORS[$&] }
#   end
# end


#
#
# class WordProblem_Other
#   NUMBER = %q(zero|one|two|three|four|five|six|seven|eight|nine)
#   OPERATORS = %q(plus|minus|divide|mult)
#   OPERATOR_CONVERSION = {'plus'=>:+, 'minus'=>:-, 'divide'=>:/, 'mult'=>:*}
#   NUM_CONV = %w(zero one two three four five six seven eight nine)
#   def initialize(str)
#     @str = str
#   end
#
#   def answer
#     parse_string
#     convert_regex_data
#     @operator = OPERATOR_CONVERSION[@operator]
#     puts @nums.reduce(@operator)
#   end
#
#   private
#
#   def parse_string
#     parses = @str.match(/(#{NUMBER}).*?(#{OPERATORS}).*?(#{NUMBER})/).captures
#     @nums, @operator = [parses[0],parses[2]], parses[1]
#   end
# end
