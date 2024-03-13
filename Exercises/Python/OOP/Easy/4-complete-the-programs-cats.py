'''
Consider the following program.
'''

'''
Update this code so you see the following output when you run the code:

    My cat Cocoa is 3 years old and has black fur.
    My cat Cheddar is 4 years old and has yellow and white fur.
'''

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def info(self):
        return f"My cat {self.name} is {self.age} and has {self.color}"

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)
