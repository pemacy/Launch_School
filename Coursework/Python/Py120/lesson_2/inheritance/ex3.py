class Dog:
    def __init__(self):
        self.species = 'Dog'

    def show_species(self):
        print(self.species)

d = Dog()
d.show_species()
d.species = 'Cat'
d.show_species()
