'''
Given the following code, modify Truck.start_engine by appending 'Drive fast, please!' to the return value of Vehicle.start_engine. The 'fast' in 'Drive fast, please!' should be taken from the value of the speed argument.
'''

class Vehicle:
    def __init__(self, year):
        self._year = year

    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        return super().start_engine() + f" Drive {speed} please!"

truck1 = Truck(1994)
print(truck1.start_engine('fast'))

truck2 = Truck(2002)
print(truck2.start_engine('slow'))
