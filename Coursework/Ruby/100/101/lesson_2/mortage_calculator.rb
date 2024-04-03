# mortgage_calculator.rb

def prompt(message)
  puts "==>  #{message}"
end

def display_data(loan, years_months, apr)
  <<-DATA

    Loan: $#{loan}
    Years: #{years_months[0]}
    Months: #{years_months[1]}
    APR: %#{apr}

  DATA
end


# ===== GET USER DATA =====
def welcome
  prompt("Welcome to the monthly payment calculator!")
  loop do
    prompt("Please enter your name:")
    name = gets.chomp.strip
    if !name.empty?
      return name
    else
      prompt("There was nothing entered")
    end
  end
end

def get_loan
    prompt("== Enter Loan Amount ==")
    loop do
      print("Loan Amount:  $")
      loan = gets.chomp.strip.delete('$').delete(',')
      if positive_number?(loan)
        return loan
      else
        prompt("Invalid Loan Amount, please try again")
      end
    end
end

def get_duration
  prompt("== Enter length of loan in Years and Months ==")
  loop do
    print("Years:  ")
    years = gets.chomp.strip
    print("Months:  ")
    months = gets.chomp.strip
    if positive_integer?(years) && positive_integer?(months)
      return [years, months]
    else
      prompt("Invalid entry, or 0 entered for both values, please try again")
    end
  end
end

def get_apr
  prompt("== Enter APR ==")
  loop do
    print("APR:  %")
    apr = gets.chomp.strip.delete('$%')
    if apr_not_negative?(apr) && apr.to_f <= 100
      return apr
    else
      prompt("Invalid entry, please try again")
    end
  end
end

# ===== VALIDATE USER DATA =====
def number?(number)
  number.to_f.to_s == number || number.to_i.to_s == number
end

def positive_float?(value)
  number?(value) && value.to_f > 0
end

def positive_integer?(value)
  number?(value) && value.to_i > 0
end

def positive_number?(value)
  positive_float?(value) && positive_integer?(value)
end

def apr_not_negative?(apr)
  number?(apr) && apr.to_f >= 0
end

# ===== CALCULATE MONTHLY PAYMENT =====
def calc_duration(time)
  time[0].to_i * 12 + time[1].to_i
end

def apr_not_zero(loan, apr, total_duration)
  apr = apr.to_f / 100
  loan = loan.to_f
  loan * (apr / (1 - (1 + apr)**(total_duration * -1)))
end

def apr_zero(loan, total_duration)
  loan = loan.to_f
  loan / total_duration
end

# ===== WELCOME MESSAGE AND LOAN CALCULATION LOOP =====
name = welcome.capitalize

loop do
  loan = get_loan
  years_months = get_duration
  apr = get_apr
  total_duration = calc_duration(years_months)

  if apr.to_f > 0
    monthly_payment = apr_not_zero(loan, apr, total_duration)
  else
    monthly_payment = apr_zero(loan, total_duration)
  end

  prompt(display_data(loan, years_months, apr))

  prompt( "Your monthly payment for #{total_duration} months is:
          $#{monthly_payment.round(2)}")
  sleep(1)

  prompt("Would you like to calculate another monthly payment?:  ")
  calculate_again = gets.chomp.downcase
  break unless calculate_again.start_with?('y')
end

prompt("Goodbye #{name}, thank you for using the mortgage calculator")
