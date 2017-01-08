# calc_refactored.rb

# ask the user for two numbers
# ask the user for an opteraion to perform
# perform the operation on the two numbers
# output the result

require 'yaml'

CONFIG = YAML.load_file('config.yml')

def prompt(message)
  Kernel.puts("=> #{message}")
end

def valid_number?(num)
  num.to_i() != 0
end

def operation_to_message(op)
  case op
  when '1'
    'Adding'
  when '2'
    'Subtracting'
  when '3'
    'Multiplying'
  when '4'
    'Dividing'
  end
end

prompt(CONFIG['welcome'])

# instantiate name variable outside of loop for reference later
name = ''
loop do
  name = Kernel.gets.chomp()
  if name.empty?()
    prompt(CONFIG['valid_name'])
  else
    break
  end
end

prompt("Hi #{name}!")

# main loop
loop do
  # initialize variables a outside of loop
  a = ''
  b = ''

  prompt(CONFIG['enter_nums'])

  loop do
    prompt("Number 1:")
    a = Kernel.gets().chomp().to_i

    if valid_number?(a)
      break
    else
      prompt(CONFIG['val_num'])
    end
  end

  loop do
    prompt("Number 2:")
    b = Kernel.gets().chomp().to_i

    if valid_number?(b)
      break
    else
      prompt(CONFIG['val_num'])
    end
  end

  operator_prompt = <<-MSG
    What operation would you like to perform?
    1) add
    2) substract
    3) multiply
    4) divide
  MSG

  prompt(operator_prompt)

  c = ''
  loop do
    c = Kernel.gets().chomp()

    if %w(1 2 3 4).include?(c)
      break
    else
      prompt(CONFIG['val_op'])
    end
  end

  prompt("#{operation_to_message(c)} the two numbers...")
  sleep(1)

  result =  case c
            when "1"
              a + b
            when "2"
              a - b
            when "3"
              a * b
            when "4"
              a.to_f() / b.to_f()
            end

  prompt("Result is: #{result}")

  prompt(CONFIG['again'])
  answer = Kernel.gets().chomp()
  break unless answer.downcase().start_with?('y')
end

prompt(CONFIG['bye'])


def validating_decimals(input)
  val = input.to_i.split('.')
  if val.length > 1
    /^\d+$/.match(val[0]) && /^\d+$/.match(val[0])
  else
    /^\d+$/.match(input.to_i)
  end
end
