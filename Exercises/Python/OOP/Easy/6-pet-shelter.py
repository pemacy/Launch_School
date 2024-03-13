'''
Consider the following code:
'''

class Pet:
    def __init__(self, species, name):
        self._name = name
        self._species = species

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

class Owner:
    def __init__(self, name):
        self._name = name
        self.pets = []

    @property
    def name(self):
        return self._name

    def number_of_pets(self):
        return len(self.pets)

    def add_pet(self, pet):
        self.pets.append(pet)

class Shelter:
    def __init__(self):
        self.owners = set()

    def adopt(self, owner, pet):
        self.owners.add(owner)
        owner.add_pet(pet)

    def print_adoptions(self):
        for owner in self.owners:
            print(f"{owner.name} has adopted the following pets:")
            for pet in owner.pets:
                print(f"a {pet.species} named {pet.name}")
            print('\n')

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
