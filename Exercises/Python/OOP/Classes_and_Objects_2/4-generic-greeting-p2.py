'''
Using the following code, add two methods: generic_greeting and personal_greeting. The first method should be a class method and print a greeting that's generic to the class. The second method should be an instance method and print a greeting that's custom to the object.
'''

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @classmethod
    def generic_greeting(cls):
        print("I'm a cat")

    def personal_greeting(self):
        print(F"Hello, my name is {self.name}")

kitty = Cat('Sophie')

Cat.generic_greeting()
kitty.personal_greeting()
