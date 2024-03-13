'''
Using the following code, create a Towable mix-in that contains a method named tow. This method should print I can tow a trailer! when invoked. The mix-in should Include the mix-in in the Truck class.
'''

from towable import Towable

class Truck(Towable):
    pass

class Car:
    pass

# Comments show expected output
truck1 = Truck()
truck1.tow()        # I can tow a trailer!

# car1 = Car()
# car1.tow()
# AttributeError: 'Car' object has no attribute 'tow'
