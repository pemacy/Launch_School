class Dog:
    def __init__(self, breed):
        self.breed = breed

    def get_breed(self):
        return self.breed

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed

golden = Dog('Golden Retriever')
poodle = Dog('Poodle')
print(golden.get_breed())
print(poodle.get_breed())
