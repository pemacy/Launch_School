# minilang.rb

class Minilang
  VALID_INSTRUCTIONS = %w(n PUSH ADD SUB MULT DIV MOD POP PRINT)
  def initialize(instructions)
    @instructions = instructions.split
    @register = 0
    @stack = []
  end

  def eval
    return unless validate
    @instructions.each do |instruction|
      if VALID_INSTRUCTIONS.include?(instruction)
        interpret_instruction(instruction)
      elsif /\A[-+]?\d+\z/ =~ instruction
        @register = instruction.to_i
      end
    end

  end

  private

  def validate
    validity = @instructions.all? do |el|
      VALID_INSTRUCTIONS.include?(el) || el == el.to_i.to_s
    end
    unless validity
      invalid = @instructions.select do |el|
        !VALID_INSTRUCTIONS.include?(el) && !(el == el.to_i.to_s)
      end
      puts "Invalid token: #{invalid[0]}"
    end
    validity
  end

  def interpret_instruction(instruction)
    send(instruction.downcase)

    # case instruction
    # when 'PUSH' then push_method
    # when 'ADD' then add_method
    # when 'SUB' then sub_method
    # when 'MULT' then mult_method
    # when 'DIV' then div_method
    # when 'MOD' then mod_method
    # when 'POP' then pop_method
    # when 'PRINT' then print_method
    # end
  end

  def push
    @stack.push(@register)
  end

  def sub
    @register -= pop
  end

  def add
    @register += pop
  end

  def mult
    @register *= pop
  end

  def div
    @register /= pop
  end

  def mod
    @register %= pop
  end

  def pop
    @register = @stack.pop
  end

  def print
    puts @register
  end
end


Minilang.new('PRINT').eval
Minilang.new('5 PUSH 3 MULT PRINT').eval
Minilang.new('5 PRINT PUSH 3 PRINT ADD PRINT').eval
Minilang.new('-3 PUSH 5 SUB PRINT').eval
Minilang.new('-3 PUSH 5 XSUB PRINT').eval
Minilang.new('-3 PUSH 5 SUB PRINT').eval
Minilang.new('6 PUSH').eval
