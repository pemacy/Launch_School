'''
Using the following code, add a method named identify that returns the calling object
'''

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def identify(self):
        return self.__class__

kitty = Cat('Sophie')
print(kitty.identify())
