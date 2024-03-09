'''
Using the following code, add an instance method named rename that renames kitty when invoked.
'''

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def rename(self, name):
        self.name = name

kitty = Cat('Sophie')
print(kitty.name)
kitty.rename('Chloe')
print(kitty.name)
