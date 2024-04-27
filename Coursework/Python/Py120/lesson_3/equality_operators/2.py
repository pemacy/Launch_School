class Cat:
   def __init__(self, name):
        self.name = name

   def __eq__(self, other):
       if not isinstance(other, Cat):
           return NotImplemented
       return self.name.casefold() == other.name.casefold()

# Tests
don = Cat('Don')
matt = Cat('Matt')
don2 = Cat('DoN')
other = str()

print(don == matt)
print(don == don2)
print(don == other)
