'''
Given the following code, create a class named Vehicle that, upon instantiation, assigns the passed-in argument to self.year. Both Truck and Car should inherit from Vehicle.
'''

from towing_mixin import TowingMixin

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

class Truck(TowingMixin, Vehicle):
    def __init__(self, year):
        super().__init__(year)


class Car(Vehicle):
    def __init__(self, year):
        super().__init__(year)

truck1 = Truck(1984)
print(truck1.year)
print(truck1.tow())

car1 = Car(2006)
print(car1.year)
