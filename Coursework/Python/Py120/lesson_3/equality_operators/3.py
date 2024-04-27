class Cat:
    def __init__(self, name, age = 0):
        self.age = age
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name != other.name

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.age < other.age

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.age <= other.age

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.age > other.age

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.age >= other.age

# Test Cases

don = Cat('Don', 5)
matt = Cat('Matt', 7)

print(don == matt)
print(don < matt)
print(matt <= don)
