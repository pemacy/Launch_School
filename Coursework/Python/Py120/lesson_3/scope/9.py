class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self):
        super().__init__('Sparrow')

    def __str__(self):
        return F"{self.species=}"
s = Sparrow()
print(s)
