class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

    @property
    def filling(self):
        if self._filling:
            return self._filling
        return 'Plain'

    @filling.setter
    def filling(self, filling):
        self._filling = filling

    def __str__(self):
        if self.glazing:
            return F"{self.filling} with {self.glazing}"
        return F"{self.filling}"


donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing

'''
Write additional code for KrispyKreme such that the print statements will work
as shown above.
'''
