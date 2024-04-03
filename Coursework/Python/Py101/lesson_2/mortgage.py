'''
mortage.py
'''

class Loan:
    def __init__(self):
        self.loan_amount = self.enter_loan_amount()
        self.apr = self.enter_apr()
        self.loan_duration_years = self.enter_loan_duration_years()

    def enter_loan_duration_years(self):
        while True:
            years = input("Enter loan duration in years: ")
            if self.invalid_integer(years):
                print('Invalid integer, try again.')
            else:
                return int(years)

    def enter_apr(self):
        while True:
            print("Enter APR %: ")
            apr = input("Example - 5%, 2.5%: ")
            if self.invalid_float(apr):
                print('Invalid entry, try again.')
            else:
                return float(apr) / 100

    def enter_loan_amount(self):
        while True:
            amt = input("Enter loan amount: ")
            if self.invalid_float(amt):
                print('Invalid entry, try again.')
            else:
                return float(amt)

    def invalid_integer(self, int_str):
        try:
            int(int_str)
        except ValueError:
            return True

        return False

    def invalid_float(self, float_str):
        try:
            float(float_str)
        except ValueError:
            return True

        return False

    @property
    def monthly_interest_rate(self):
        return self.apr / 12

    @property
    def loan_duration_months(self):
        return self.loan_duration_years * 12

    def monthly_payment(self):
        return ( self.loan_amount *
                 (self.monthly_interest_rate /
                  (1 -
                    (self.monthly_interest_rate + 1) **
                     (-self.loan_duration_months)
                  )
                 )
                )

    def __str__(self):
        return f"Monthly Payment is: ${self.monthly_payment():.2f}"

loan = Loan()
print(loan)
