def minilang(instructions)
  instruction_array = instructions.split
  number_of_instructions = instruction_array.size
  register = 0
  stack = Array.new

  instruction_array.each do |instruction|
    case instruction
    when "PRINT" then puts "#{register}"
    when "PUSH" then stack << register.to_i
    when "POP" then register = stack.pop
    when "ADD" then register += stack.pop
    when "SUB" then register -= stack.pop
    when "MULT" then register *= stack.pop
    when "DIV" then register /= stack.pop
    when "MOD" then register %= stack.pop
    else register = instruction.to_i
    end
  end
end

minilang('PRINT')
