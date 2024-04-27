'''
Ben and Alyssa are working on a vehicle management system. So far, they have
created classes called Auto and Motorcycle to represent automobiles and
motorcycles. After having noticed common information and calculations they
were performing for each vehicle type, they decided to break the common
behaviors into a separate class called WheeledVehicle. This is what their code
looks like so far:
'''

class FueledVehicleMixin:
    def set_fuel_efficiency(self, kilometers_per_liter):
        self.fuel_efficiency = kilometers_per_liter

    def set_liters_of_fuel_capacity(self, liters_of_fuel_capacity):
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicle(FueledVehicleMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.set_fuel_efficiency(kilometers_per_liter)
        self.set_liters_of_fuel_capacity(liters_of_fuel_capacity)

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires are various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires are various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Catamaran(FueledVehicleMixin):
    def __init__(self,
               number_propellers,
               number_hulls,
               kilometers_per_liter,
               liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.set_fuel_efficiency(kilometers_per_liter)
        self.set_liters_of_fuel_capacity(liters_of_fuel_capacity)
