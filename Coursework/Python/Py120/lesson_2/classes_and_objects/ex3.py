class Person:
    def __init__(self, name):
        self._first_name = ''
        self._last_name = ''
        self.set_name(name)

    def set_name(self, name):
        if len(name.split()) < 2:
            self.first_name = name
            self.last_name = ''
        else:
            self.first_name, self.last_name = name.split()

    @property
    def name(self):
        return (self.first_name + ' ' + self.last_name).strip()

    @name.setter
    def name(self, name):
        self.set_name(name)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, fn):
        self._first_name = fn

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, ln):
        self._last_name = ln

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams
