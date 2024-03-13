'''
Consider the following classes:
'''

class WheelsMixin:
    @property
    def number_wheels(self):
        return self._number_wheels

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheets(self):
        return self.number_wheels

    def into(self):
        return f"{self.make} {self.model}"


class Car(WheelsMixin, Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self._number_wheels = 4


class Motorcycle(WheelsMixin, Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self._number_wheels = 2

class Truck(WheelsMixin, Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload
        self._number_wheels = 6
