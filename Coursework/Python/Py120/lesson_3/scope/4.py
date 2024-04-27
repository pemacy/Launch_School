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

golden = Dog('Golden')
golden.breed = 'Oxford'
print(golden.get_breed())
