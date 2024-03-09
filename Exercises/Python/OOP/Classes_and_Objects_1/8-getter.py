'''
Using the code snippet provided below, add a getter method named name and invoke it in place of self._name in greet.
'''

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello my name is {self.name}")

kitty = Cat('Sophie')
kitty.greet()
