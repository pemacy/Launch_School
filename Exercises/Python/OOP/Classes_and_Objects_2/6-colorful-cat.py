'''
Create a class named Cat that prints a greeting when the greet instance method is invoked. The greeting should include the name and color of the cat. Use a class constant to define the color.
'''

class Cat:
    color = 'purple'

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def greet(self):
        print(f"Hello my name is {self.name} and I'm a {Cat.color} cat!")

kitty = Cat('Sophie')
kitty.greet()
