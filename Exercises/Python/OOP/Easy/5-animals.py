'''
Given the following Animal class, create two more classes, Cat and Dog, that inherit from it:
'''

class Animal:
    def __init__(self, name, age, legs, species, status):
        self._name = name
        self._age = age
        self._legs = legs
        self._species = species
        self._status = status

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def legs(self):
        return self._legs

    @property
    def species(self):
        return self._species

    @property
    def status(self):
        return self._status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")

class Cat(Animal):
    def __init__(self, name, age, status):
        super().__init__(name, age, 4, 'cat', status)
        self._sound = 'Meow meow!'

    @property
    def sound(self):
        return self._sound

    def introduce(self):
        return super().introduce() + f" {self.sound}"

class Dog(Animal):
    def __init__(self, name, age, status, owner):
        super().__init__(name, age, 4, 'cat', status)
        self._owner = owner
        self._sound = 'Woof! Woof!'

    @property
    def owner(self):
        return self._owner

    @property
    def sound(self):
        return self._sound

    def introduce(self):
        return super().introduce() + f" {self.sound}"

    def greet_owner(self):
        return f"Hi {self.owner}! {self.sound}"

cat = Cat("Pepe", 4, "happy")
expected = ("Hello, my name is Pepe and I am 4 years old "
            "and happy. Meow meow!")
print(cat.introduce() == expected)      # True

dog = Dog("Bobo", 9, "hungry", "Daddy")
expected = ("Hello, my name is Bobo and I am 9 years old "
            "and hungry. Woof! Woof!")
print(dog.introduce() == expected)                  # True
print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True
