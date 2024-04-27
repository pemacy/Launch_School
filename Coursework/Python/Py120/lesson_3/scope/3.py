class Cat:
    def __init__(self, name = None):
        if name:
            self.name = name
        else:
            print('Name not set!')

    def get_name(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

c = Cat('c')
print(c.get_name())
c2 = Cat()
