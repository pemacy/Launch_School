# loan_calc.rb

# calculates the apr each month and determines monthly payments

require 'yaml'

MSG = YAML.load_file('loan_calc.yml')

def prompt(message)
  puts("==> #{message}")
end

#  ======= VALIDATE input data =======
def validate_months_or_years(num)
  if num.positive? &&

def validate_loan_amount_with_regex(num)
  /^(\$)?[0-9]{1,3}(?:,?[0-9]{3})*(?:\.[0-9]{2})?$/ =~ num
  # (/$)? - 1st capturing group entered 0 or 1 times, dollar sign
  # [0-9]{1,3} - a single digit repeated 1-3 times
  # (?: ) - non-capturing group
    # ,? - comma is optional
    # [0-9]{1,3} - a single digit repeated 1-3 times
  # * - non-capturing group can be repeated zero to unlimited times
  # (?: ) - non-capturing group
    #\.[0-9]{2} - decimal followed by 2 digits
  # ? - non-capturing group can be given 0 to 1 times
end

def valid_int?(num)
  /^(\$))\d+$/.match(num)
end

def valid_float?(num)
  /^\d+\.?(\d{0,2})?$/.match(num)
end

def int_if(message)
  loop do
    prompt(message)
    input = gets.chomp
    if valid_int?(input)
      return input
    else
      prompt(MSG['bad_num_value'])
    end
  end
end

def float_if(message)
  loop do
    prompt(message)
    input = gets.chomp
    if valid_float?(input)
      return input
    else
      prompt(MSG['bad_num_value'])
    end
  end
end

prompt(MSG['welcome'])

loop do
  # SET loan_amount, apr, loan_duration_years, loan_duration_months
  loan_amount = float_if(MSG['input_amt'])

  loan_duration_years = int_if(MSG['input_years'])

  loan_duration_months = int_if(MSG['input_months'])

  apr = float_if(MSG['input_apr'])

  # calculate variables to use in monthly payment calculation
  total_loan_duration_months =  loan_duration_years.to_i * 12 +
                                loan_duration_months.to_i
  monthly_interest_rate = apr.to_f / 100 / 12

  # show data entered
  data = <<-DATA
  Data:
    APR: #{apr}%
    Years: #{loan_duration_years}
    Months: #{loan_duration_months}
    Amount: $#{loan_amount}.00
    Monthly Interest Rate: #{(monthly_interest_rate * 100).round(2)}%
    Loan Duration Months: #{total_loan_duration_months}
  DATA

  prompt(data)

  # calculate the monthly payment
  m = loan_amount.to_f * (monthly_interest_rate.to_f / (1 - (1 +
      monthly_interest_rate.to_f)**(total_loan_duration_months.to_f * -1)))

  # dramatic effect
  sleep(1)

  # show monthly payment
  prompt("Monthly payment is $#{m.round(2)}")

  # dramatic effect
  sleep(1)

  prompt(MSG['again'])
  again = gets.chomp
  break unless again.downcase.start_with?('y')
end
