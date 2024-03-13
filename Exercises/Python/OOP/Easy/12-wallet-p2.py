'''
Using the code from the previous exercise, modify the code so that when we print the merged_wallet we receive a message Wallet with $80.
'''

class Wallet:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented

        return Wallet(self.amount + other.amount)

    def __str__(self):
        return f"Wallet with ${self.amount}"

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)          # Wallet with $80.
