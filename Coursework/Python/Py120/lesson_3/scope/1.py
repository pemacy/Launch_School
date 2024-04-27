class Dog:
    def __init__(self, breed):
        self.breed = breed

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed

    def __str__(self):
        return F"I am a {self.breed}."

golden = Dog('Golden Retriever')
poodle = Dog('Poodle')
print(golden)
print(poodle)

