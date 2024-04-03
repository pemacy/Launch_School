# loan_calc.rb

require 'yaml'
MSG = YAML.load_file('loan_calc.yml')

def prompt(message)
  puts("==> #{message}")
end

# ======= Get input data methods =======
def get_name(message)
  loop do
    prompt(message)
    name = gets.chomp
    if /^[a-zA-z]*(\s[a-zA-Z]*)?$/ =~ name.strip
      return name
    else
      prompt(MSG['bad_name'])
    end
  end
end

def get_loan(message)
  loop do
    prompt(message)
    loan = gets.chomp
    if valid_loan_amount?(loan)
      return loan.delete(',').delete('$').to_f.round(2)
    else
      prompt(MSG['bad_num_value'])
    end
  end
end

def get_month_or_year(message)
  loop do
    prompt(message)
    input = gets.chomp
    if validate_months_or_years?(input)
      return input.to_i
    else
      prompt(MSG['bad_num_value'])
    end
  end
end

def get_apr(message)
  loop do
    prompt(message)
    apr = gets.chomp
    if valid_apr?(apr)
      return apr.delete('%').to_f
    else
      prompt(MSG['bad_num_value'])
    end
  end
end

#  ======= VALIDATE input data methods =======
def validate_months_or_years?(num)
  num.to_i.integer?
end

def validate_loan_amount_with_regex(num)
  /^(\$)?[0-9]{1,3}(?:,?[0-9]{3})*(?:\.[0-9]{2})?$/ =~ num
  # (/$)? - 1st capturing group entered 0 or 1 times, dollar sign
  # [0-9]{1,3} - a single digit repeated 1-3 times
  # (?: ) - non-capturing group
    # ,? - comma is optional
    # [0-9]{1,3} - a single digit repeated 1-3 times
  # * - non-capturing group can be repeated zero to unlimited times
  # (?: ) - non-capturing group
    # \.[0-9]{2} - decimal followed by 2 digits
  # ? - non-capturing group can be given 0 to 1 times
end

def valid_loan_amount?(loan)
  loan.delete(',').delete('$').to_f.positive?
end

def valid_apr?(apr)
  /^%?\.?([0-9]{1,2})(\.[0-9]{1,3})?$/.match(apr)
  # %? - percent sign optional
  # \.? - leading decimal optional
  # ([0-9]){1,2}) - up to 2 positive numbers mandatory
  # (\.[0-9]{1,3})? - up to 3 trailing numbers following a decimal optional
end

# ======= Welcome Message And Loan Loop=======
name = get_name(MSG['welcome'])

loop do
  loan_amount = get_loan(MSG['input_amt'])
  loan_duration_years = ''
  loan_duration_months = ''
  loop do
    loan_duration_years = get_month_or_year(MSG['input_years'])
    loan_duration_months = get_month_or_year(MSG['input_months'])
    prompt("Years or Months must be greater than 0") if loan_duration_years +
                                                        loan_duration_months < 1
    break unless loan_duration_years + loan_duration_months < 1
  end
  apr = get_apr(MSG['input_apr'])

  # calculate variables to use in monthly payment calculation
  total_loan_duration_months =  loan_duration_years * 12 + loan_duration_months
  monthly_interest_rate = apr / 100 / 12 if apr >= 1

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
  if apr > 0
    m = loan_amount * (monthly_interest_rate / (1 - (1 +
        monthly_interest_rate)**(total_loan_duration_months * -1)))
  else
    m = loan_amount / total_loan_duration_months
  end

  # show monthly payment
  prompt("#{name}, your monthly payment is $#{m.round(2)}")

  # dramatic effect
  sleep(1)

  prompt(MSG['again'])
  again = gets.chomp
  break unless again.downcase.start_with?('y')
end
