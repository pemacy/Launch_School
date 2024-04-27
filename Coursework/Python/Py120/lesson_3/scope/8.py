class Car:
    manufacturer = 'Ford'
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(F"{self.manufacturer=}")
        print(F"{self.__class__.manufacturer=}")

c = Car('Chevy')
c.show_manufacturer()
