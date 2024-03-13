'''
Using the following code, create a mix-in named WalkingMixin that contains a method named walk. This method should print Let's go for a walk! when invoked. Include WalkingMixin in Cat.
'''

from walking_mixin import WalkingMixin

class Cat(WalkingMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello, my name is {self.name}")

kitty = Cat('Sophie')
kitty.greet()
kitty.walk()
